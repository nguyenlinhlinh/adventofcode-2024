import heapq
import sys
from collections import defaultdict

def getInputs(file):
    gates = {}
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
            gates[gate] = int(value.strip(" "))
    return (gates, operations)

def execute(gates, operations):
    while operations:
        (a, op, b, c) = operations.pop(0)
        if a  not in gates or b not in gates:
            operations.append((a, op, b, c))
            continue
        if op == 'AND':
            gates[c] = gates[a] & gates[b]
        elif op == 'OR':
            gates[c] = gates[a] | gates[b]
        elif op == 'XOR':
            gates[c] = gates[a] ^ gates[b]

if __name__ == "__main__":
    file = open("24/input.txt", "r")
    (gates, operations) = getInputs(file)
    execute(gates, operations)
    result = []
    for k, v in gates.items():
        if k.startswith('z'):
            result.append((k, v))
    result.sort(reverse=True, key=lambda a: a[0])
    string = [str(v)  for (k, v) in result]
    print("Decimal value of z", int("".join(string), 2))
    
# solution 47666458872582
