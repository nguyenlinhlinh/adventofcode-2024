f= open("15/input.txt", "r")

WALL = '#'
BOX = 'O'
ROBOT = '@'
DIR = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
BIGGER_BOX = ['[',']']

def getInputs():
    startPosition = None
    obsticals = {}
    directions = []
    rows = 0
    cols = 0
    boxFinder = {}
    for line in f:
        line = line.strip().replace('\n', "")
        if line.startswith(WALL):
            cols = len(line) * 2
            c = 0
            for char in line:
                firstHalf = (rows, c)
                secondHalf = (rows, c + 1)
                if char == ROBOT:
                    startPosition = firstHalf
                elif char == WALL:
                    obsticals[firstHalf] = char
                    obsticals[secondHalf] = char
                elif char == BOX:
                    obsticals[firstHalf] = '['
                    obsticals[secondHalf] = ']'
                    boxFinder[firstHalf] = secondHalf
                    boxFinder[secondHalf] = firstHalf
                c+=2
            rows += 1
                
        elif len(line) > 0:
            for char in line:
                directions.append(DIR[char])
    return (startPosition, obsticals, boxFinder, directions, rows, cols)
    

def isInSideTheMap(pos, rows, cols):
    return pos[0] in range(rows) and pos[1] in range(cols)

def isBox(pos):
    return pos in obsticals and obsticals[pos] != WALL

def findAllEffectedBoxes(robotPos, dir, boxFinder, rows, cols):
    (r, c) = robotPos
    (dR, dC) = dir
    queue = [(r + dR, c + dC)]
    effectedBoxes = set()
    visited = set()
    while len(queue) > 0:
        pos = queue.pop()
        if pos in visited:
            continue
        visited.add(pos)
        if isBox(pos):
            effectedBoxes.add(pos)
            otherHalf = boxFinder[pos]
            if otherHalf not in visited:
                queue.append(otherHalf)
        nextPos = (pos[0] + dR, pos[1] + dC)
        if not isInSideTheMap(nextPos, rows, cols) or nextPos in visited:
            continue
        if isBox(nextPos):
            queue.append(nextPos)
    return effectedBoxes

def canPush(boxes, dir):
    (rD, cD) = dir
    for pos in boxes:
        (r, c) = pos
        nextPos = (r + rD, c + cD)
        if obsticals.get(nextPos) == WALL: # Hit a wall
            return False
        if isBox(nextPos) and not nextPos in boxes: # Hit a box that is not in the effected box
            return False
    return True

def push(boxes, dir, boxFinder):
    (rD, cD) = dir
    oldPositions = boxes.copy()
    newPositions = set()
    newBoxFinder = {}
    # get the new positions for boxes
    while boxes:
        first = boxes.pop()
        second = boxFinder[first]
        boxes.remove(second)
        firstHalf = obsticals[first]
        secondHalf = obsticals[second]
        newFirstPos = (first[0] + rD, first[1] + cD)
        newSecondPos = (second[0] + rD, second[1] +cD)
        newPositions.add((newFirstPos, firstHalf))
        newPositions.add((newSecondPos, secondHalf))
        newBoxFinder[newFirstPos] = newSecondPos
    positions = [pos[0] for pos in newPositions]

    # Find positions that no longer have obsticals in and remove those from boxFinder and obsticals
    for position in oldPositions:
        if not position in positions:
            del boxFinder[position]
            del obsticals[position]
    # Update obsticals and boxFinder with new box positions info
    for (position, value) in newPositions:
        obsticals[position] = value
    for first, second in newBoxFinder.items():
        boxFinder[first], boxFinder[second] = second, first

def simulateRobotMovements(boxFinder, rows, cols):
    currentPos = startPosition
    for dir in directions:
        nextPos = (currentPos[0] + dir[0], currentPos[1]+ dir[1])
        if not isInSideTheMap(nextPos, rows, cols) or obsticals.get(nextPos) == WALL:
            continue
        if  nextPos not in obsticals:
            currentPos = nextPos
            continue
        boxes = findAllEffectedBoxes(currentPos, dir, boxFinder, rows, cols)
        if canPush(boxes, dir):
            push(boxes, dir, boxFinder)
            currentPos = nextPos
  
def calculateSumOfBoxCoordinates():
    total = 0
    for pos, obstical in obsticals.items():
        (r, c) = pos
        if obstical == '[':
            total += 100 * r + c
    return total

if __name__ == "__main__":
    (startPosition, obsticals, boxFinder, directions, rows, cols) = getInputs()
    simulateRobotMovements(boxFinder, rows, cols)
    total = calculateSumOfBoxCoordinates()
    print("sum of all boxes", total)

# solution 1519202