import heapq
import sys
from collections import defaultdict

def getInputs(file):
    x = []
    y = []
    operations = []
    parsingGates = True
    for line in file.readlines():
        if line == '\n':
            parsingGates = False
            continue
        line = line.strip().replace("\n", "")
        if not parsingGates:
            [a, op, b, c] = [i.strip() for i in line.split(" ") if i != '->']
            operations.append((a, op, b, c))
            continue
        if parsingGates == True:
            (gate, value) = line.split(":")
            if gate.startswith('x'):
                x.append(gate)
            elif gate.startswith('y'):
                y.append(gate)
    x.sort()
    y.sort()
    return (operations, x, y)

def execute(gates, operations):
    ops = operations.copy()
    sortedOperation = []
    count = 0
    while ops:
        count +=1
        (a, op, b, c) = ops.pop(0)
        if a  not in gates or b not in gates:
            ops.append((a, op, b, c))
            if count > 10:
                break
            continue
        sortedOperation.append((a, op, b, c))
        if op == 'AND':
            gates[c] = gates[a] & gates[b]
        elif op == 'OR':
            gates[c] = gates[a] | gates[b]
        elif op == 'XOR':
            gates[c] = gates[a] ^ gates[b]
    return sortedOperation

# Test if the operations give correct result
def hasCorrecOutPut(sumGate, carryGate, prevCarry, operations, x, y):
    if not sumGate.startswith('z'):
        return False
    # (x, y, carry)
    testValues = [(1, 1, 1), (1, 1, 0), (1, 0, 1), (1, 0, 0), (0, 1, 1), (0, 1, 0), (0,0,1),(0,0, 0)]
    # (sum, carry)
    expectedValues = [(1, 1), (0, 1), (0,1), (1, 0), (0,1), (1, 0), (1, 0), (0, 0)]
    # (sum, carry)
    noCarryExpectedValues = [(0, 1), (0, 1), (1,0), (1, 0), (1,0), (1, 0), (0, 0), (0, 0)]
    for i in range(len(testValues)):
        (tX, tY, tC) = testValues[i]
        gates = {x: tX, y: tY}
        if prevCarry != None:
            gates[prevCarry] = tC
        execute(gates, operations)
        (expectSum, expectedCarry) =  expectedValues[i] if prevCarry else noCarryExpectedValues[i]
        if gates[sumGate] != expectSum or (gates[carryGate] != expectedCarry):
            return False
    return True

# Get all operations related to initial gates
def getRelatedOperations(initialGates, operations):
    gates = set(initialGates)
    operands = set(initialGates)
    ops = []
    oldLen = 0
    while oldLen < len(gates):
        oldLen = len(gates)
        for (a, op, b, c) in operations:
            if (a, op, b, c) not in ops and a in gates and b in gates:
                ops.append((a, op, b, c))
                operands.add(a)
                operands.add(b)
                gates.add(c)
    return (ops, operands)

# Swap two output gates at a time and check if it provide a correct result
def checkOutputs(operations, operands, x, y, prevCarry):
    for i in range(len(ops)):
        for j in range(len(ops)):
            newOps = operations.copy()
            if i != j:
                (a1, op1, b1, c1) = newOps[i]
                (a2, op2, b2, c2) = newOps[j]
                newOps[i] = (a1, op1, b1, c2)
                newOps[j] = (a2, op2, b2, c1)
            sumGate = None
            carryGate = None
            for (a, op, b, c) in newOps:
                if op not in operands:
                    if op == 'XOR':
                        sumGate = c
                    else:
                        carryGate = c
            if hasCorrecOutPut(sumGate, carryGate, prevCarry, newOps, x, y):
                if i != j:
                    return (carryGate, ops[i][3], ops[j][3])
                return (carryGate, None, None)

if __name__ == "__main__":
    file = open("24/input.txt", "r")
    (operations, xGates, yGates) = getInputs(file)
    carryGate = None
    result = []
    for i in range(len(xGates)):
        initialGates = [xGates[i], yGates[i]]
        if carryGate:
            initialGates.append(carryGate)
        (ops, operands) = getRelatedOperations(initialGates, operations)
        (carryGate, op1, op2) = checkOutputs(ops, operands, xGates[i], yGates[i], carryGate)
        if op1 and op2:
            result.append(op1)
            result.append(op2)
    result.sort()
    print("Wires involved in a swap", ",".join(result))
    
# solution dnt,gdf,gwc,jst,mcm,z05,z15,z30
