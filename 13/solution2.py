import sys
f= open("13/input.txt", "r")

machines = []
currMachine = []
for line in f:
    if line.startswith("Button"):
        currMachine.append([int(value.split("+")[1]) for value in line.strip().split(":")[1].split(",")])
    elif line.startswith("Prize"):
        prize = [ int(value.split("=")[1]) for value in line.strip().split(":")[1].split(",")]
        currMachine.append(prize)
        machines.append((currMachine[0], currMachine[1], currMachine[2]))
        currMachine = []

totalTokens = 0

for machine in machines:
    [buttonA, buttonB, prize] = machine
    (xA, yA) = buttonA
    (xB, yB) = buttonB

    (x,y) = [i + 10000000000000 for i in prize]
    bTimes = (x * yA - xA* y)/(yA*xB - (xA*yB))
    aTimes = (y - yB*bTimes)/yA

    if bTimes > 0 and aTimes > 0 and bTimes.is_integer() and aTimes.is_integer():
        tokens = int(aTimes)*3 + int(bTimes) * 1
        totalTokens += tokens

print(totalTokens)
# solution 101726882250942