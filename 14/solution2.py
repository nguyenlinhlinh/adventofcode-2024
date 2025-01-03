# Solved by finding the lowest average distance between the robots
# The idea is when the robots forms a xmas tree they will be close to each others.
# This is only true if they doesn't form a circle of something with minimal avg distance
# If that is the case maybe needs to store 10 or 100 minimal average distances to have visual inspection of the positions

import sys
f= open("14/input.txt", "r")

def getPositionAndVelocity():
    positions = []
    velocities = []
    for line in f:
        data = [i.split("=")[1].split(",") for i in line.strip().split(" ")]
        pos = (int(data[0][0]), int(data[0][1]))
        velocity = (int(data[1][0]), int(data[1][1]))
        positions.append(pos)
        velocities.append(velocity)
    return (positions, velocities)
    
def hasSamePositions(startPositions, currenPositions):
    if len(startPositions) != len(currenPositions):
        return False
    for i in range(len(startPositions)):
        if currenPositions[i] != startPositions[i]:
            return False
    return True

# Initial solution but very slow. Calculate average distance of a point to all other points   
def findAvgDistance(positions):
    totalAvgDis = 0
    for i in range(len(positions)):
        p1 = positions[i]
        totalDis = 0
        for j in range(len(positions)):
            if i == j:
                continue
            p2 = positions[j]
            distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
            totalDis += distance
        totalAvgDis += (totalDis / len(positions))
    return totalAvgDis/len(positions)

# Talked to a colleague which recommend this one to make it quicker. Calculate distance of all point to middle point
def findAvgDistanceToMiddlePoint(positions, middlePoint):
    totalDis = 0
    (mX, mY) = middlePoint
    for i in range(len(positions)):
        (x, y) = positions[i]
        distance = abs(x - mX) + abs(y - mY)
        totalDis += distance
    return totalDis/len(positions)

def simulateNextSecond(currentPosisitions, velocity, wide, tall):
    nextPosistions = []
    for i in range(len(currentPosisitions)):
        (x, y) = currentPosisitions[i]
        (vX, vY) = velocity[i]
        nextPos = ((x + vX) % wide, (y + vY)%tall)
        nextPosistions.append(nextPos)
    return nextPosistions

def findXmasTree(positions, velocity, wide, tall):
    startPositions = [pos for pos in positions]
    currentPositions = startPositions
    seconds = 1
    minAvgDis = (sys.maxsize, seconds, startPositions)
    while True:
        currentPositions = simulateNextSecond(currentPositions, velocity, wide, tall)
        avgDis = findAvgDistanceToMiddlePoint(currentPositions, (wide // 2, tall // 2))
        if avgDis < minAvgDis[0]:
            minAvgDis = (avgDis, seconds, currentPositions)
        if hasSamePositions(startPositions, currentPositions):
            break
        seconds += 1
    return minAvgDis

if __name__ == "__main__":
    wide = 101
    tall = 103
    (positions, velocity) = getPositionAndVelocity()
    (avg, seconds, positions) = findXmasTree(positions, velocity, wide, tall)
    print("seconds", seconds)

# solution 6532
