import sys
f= open("14/input.txt", "r")
wide = 101
tall = 103

safetyFactor = 0
robots = []

for line in f:
    numbers = [i.split("=")[1].split(",") for i in line.strip().split(" ")]
    pos = (int(numbers[0][0]), int(numbers[0][1]))
    velocity = (int(numbers[1][0]), int(numbers[1][1]))
    robots.append([pos, velocity])

def calculateSafetyFactor():
    first, second, third, fourth = 0,0,0,0
    xMid =  wide // 2
    yMid = tall // 2
    for robot in robots:
        (x, y) = robot[0]
        if x < xMid and y < yMid:
            first += 1
        elif x > xMid and y < yMid:
            second += 1
        elif x < xMid and y > yMid:
            third += 1
        elif x > xMid and y > yMid:
            fourth += 1
    safetyFactor = first * second * third * fourth
    print("safetyFactor", safetyFactor)

for second in range(100):
    for robot in robots:
        (x, y) = robot[0]
        (vX, vY) = robot[1]
        nextPos = ((x + vX) % wide, (y + vY)%tall)
        robot[0] = nextPos
    calculateSafetyFactor()





print("safetyFactor", safetyFactor)
# solution 230900224
