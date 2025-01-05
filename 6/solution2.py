UP = (-1, 0)

def getInputs(file):
    obsticals = set()
    startPos = (0,0)
    currentDir = UP
    rows = 0
    cols = 0
    for line in file:
        cols = 0
        for char in line.strip():
            if char== "^":
                startPos = (rows, cols)
            if char == "#":
                obsticals.add((rows, cols))
            cols += 1
        rows += 1
    return (startPos, currentDir, obsticals, rows, cols)

def isInsideMap(pos, rows, cols): 
    return pos[0] in range(rows) and pos[1] in range(cols)

def hasCircle(startPos, currDir, obsticals, rows, cols):
    visited = set()
    currPos = startPos
    while isInsideMap(currPos, rows, cols):
        if (currPos, currDir) in visited:
            return True
        visited.add((currPos, currDir))
        (r,c) = currPos
        (dR, dC) = currDir
        nexPost = (r + dR, c + dC)
        if nexPost in obsticals:
            currDir = (dC, -dR)
        else:
            currPos = nexPost
    return False

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

    return positions

if __name__ == "__main__":
    file = open("6/input.txt", "r")
    (startPos, currentDir, obsticals, rows, cols) = getInputs(file)
    positions = getDistinctPositions(startPos, currentDir, obsticals, rows, cols)
    options = 0
    count = len(positions)
    for pos in positions:
        obsticals.add(pos)
        if hasCircle(startPos, currentDir, obsticals, rows, cols):
            options += 1
        obsticals.remove(pos)
        count -= 1
    print(options)

# solution 1697
