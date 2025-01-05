import re

f= open("6/input.txt", "r")

UP = (-1, 0)
def getInputs():
    obsticals = set()
    startPos = (0,0)
    rows = 0
    cols = 0
    for line in f:
        cols = 0
        for char in line.strip():
            if char== "^":
                startPos = (rows, cols)
                currentDir = UP
            if char == "#":
                obsticals.add((rows, cols))
            cols += 1
        rows += 1
    return (startPos, currentDir, obsticals, rows, cols)

def isInsideMap(pos, rows, cols): 
    return pos[0] in range(rows) and pos[1] in range(cols)

def getDistinctPositions(startPos, currentDir, obsticals, rows, cols):
    positions = set()
    currPos = startPos
    currDir = currentDir

    while isInsideMap(currPos, rows, cols):
        (r, c) = currPos
        (dR, dC) = currDir
        positions.add(currPos)
        (nR, nC) = (r + dR,  c + dC)
        if isInsideMap((nR, nC), rows, cols) and (nR, nC) in obsticals:
            currDir = (dC, -dR) # turn right 90 
        else:
            currPos = (nR, nC)
    return len(positions)

if __name__ == "__main__":
    (startPos, currentDir, obsticals, rows, cols) = getInputs()
    result = getDistinctPositions(startPos, currentDir, obsticals, rows, cols)
    print("Number of distinct postions", result)

# solution 4988
