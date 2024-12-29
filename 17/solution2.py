
operands = { 4: "A", 5: "B", 6: "C" }

def getInputs(file):
    registers = {}
    program = []
    for line in file:
        line = line.strip()
        if line.startswith("Register"):
            (register, value) = line.split(":")
            registers[register.split(" ")[1]] = int(value.strip())
        elif len(line) > 0:
            program = [int(i) for i in line.split(":")[1].split(",")]
    return (registers, program)

def getComboOperand(operand, registers):
    if operand in range(4):
        return operand
    return registers[operands[operand]]

def execute (registers, program):
    instructionPointer = 0
    out = []
    while instructionPointer < len(program) - 1:
        opcode = program[instructionPointer]
        operand = program[instructionPointer + 1]
        if opcode == 0:
            numerator = registers["A"]
            denominator = pow(2, getComboOperand(operand, registers))
            registers["A"] = numerator // denominator
        if opcode == 1:
            x = registers["B"]
            registers["B"] = x^operand
        if opcode == 2:
            registers["B"] = getComboOperand(operand, registers) % 8
        if opcode == 3:
            if registers["A"] != 0:
                instructionPointer = operand
                continue
        if opcode == 4:
            x = registers["B"]
            y = registers["C"]
            registers["B"] = x^y
        if opcode == 5:
            out.append(str(getComboOperand(operand, registers)%8))
        if opcode == 6:
            numerator = registers["A"]
            denominator = pow(2, getComboOperand(operand, registers))
            registers["B"] = numerator // denominator
        if opcode == 7:
            numerator = registers["A"]
            denominator = pow(2, getComboOperand(operand, registers))
            registers["C"] = numerator // denominator
        instructionPointer += 2
    return out

# The idea is to only care about the out operation that module with 8. Since it is where the output is controlled.
# Based on that I realize that the number should be something multiplies with 8 (k*8) and used that factor to find where the search range should start.
# The search start with number 0 and expect output is the last number in program. Once it find the A number that output the first number in the program it multiply that A number with 8.
# Search for the next number in the program start from A * 8 and expected is now the two last numbers in program. This continue until finding the A number that produce the sequence in the program.

def findValueOfA(program):
    start = len(program) - 1
    expected = str(program[-1])
    A = 0
    while True:
        registers["A"] = A
        out = execute(registers, program)
        if ",".join(out) == expected:
            if len(out) == len(program):
                return A
            else:
                start -= 1
                expected = ",".join([str(i) for i in program[start:]])
                A = A * 8
                continue
        A += 1

if __name__ == "__main__":
    file= open("17/input.txt", "r")
    (registers, program) = getInputs(file)
    A = findValueOfA(program)
    print("register A should be", A)

# solution 164541160582845