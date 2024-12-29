

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

operands = { 4: "A", 5: "B", 6: "C" }

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

if __name__ == "__main__":
    file= open("17/input.txt", "r")
    (registers, program) = getInputs(file)
    out = execute(registers, program)
    print("out", ",".join(out))
 
# solution 6,4,6,0,4,5,7,2,7