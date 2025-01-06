import sys


WALL = '#'
BOX = 'O'
ROBOT = '@'
EMPTY = '.'


DIR = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
def getInputs(file):
    startPosition = None
    obsticals = {}
    directions = []
    rows = 0
    cols = 0
    for line in file:
        line = line.strip().replace('\n', "")
        if line.startswith(WALL):
            cols = len(line)
            for c in range(len(line)):
                char = line[c]
                if char == ROBOT:
                    startPosition = (rows, c)
                elif char == WALL or char == BOX:
                    obsticals[rows, c] = char
            rows += 1
                
        elif len(line) > 0:
            for char in line:
                directions.append(DIR[char])
    return (startPosition, obsticals, directions, rows, cols)

def isInSideTheMap(pos, rows, cols):
    return pos[0] in range(rows) and pos[1] in range(cols)

def push(dir, pos, obsticals, rows, cols):
    (dR, dC) = dir
    emptySlot = None
    currPos = (pos[0] + dR, pos[1] + dC)
    # Find an empty slot
    while isInSideTheMap(currPos, rows, cols):
        if currPos in obsticals:
            emptySlot = currPos
            break
        if obsticals[currPos] == WALL:
            break
        currPos = (currPos[0] + dR, currPos[1] + dC)
    # if there is an empty slot move obstical one by one.
    if emptySlot != None:
      (opR, opC) = (dir[0] * -1, dir[1]* -1)
      while emptySlot != pos:
            (eR, eC) = emptySlot
            prevEmptySlot = (eR + opR, eC + opC)
            if prevEmptySlot in obsticals:
                obstical = obsticals[prevEmptySlot]
                del obsticals[prevEmptySlot]
                obsticals[emptySlot] = obstical
            emptySlot = prevEmptySlot

def simulateRobotMovements(startPosition, directions, obsticals, rows, cols):
    currentPos = startPosition
    for dir in directions:
        (r, c) = currentPos
        (dR, dC) = dir
        nextPos = (r + dR, c + dC)
        if isInSideTheMap(nextPos, rows, cols):
            push(dir, currentPos, obsticals, rows, cols)
            if not nextPos in obsticals:
                currentPos = nextPos    

def calculateSumOfBoxCoordinates(obsticals):
    total = 0
    for pos, obstical in obsticals.items():
        (r, c) = pos
        if obstical == BOX:
            total += 100 * r + c
    return total

if __name__ == "__main__":
    file = open("15/input.txt", "r")
    (startPosition, obsticals, directions, rows, cols) = getInputs(file)
    simulateRobotMovements(startPosition, directions, obsticals, rows, cols)
    total = calculateSumOfBoxCoordinates(obsticals)
    print("total", total)
# solution 1490942
