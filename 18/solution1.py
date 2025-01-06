import sys
import heapq
WALL = '#'
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
directions = [UP, DOWN, LEFT, RIGHT]

def getInputs(file):
    bytePositions = []
    for line in file:
        [x, y] = line.strip().replace('\n', "").split(",")
        bytePositions.append((int(x), int(y)))
    return bytePositions

def isInSideTheMap(pos):
    return pos[0] in range(rows) and pos[1] in range(cols)

def BFS(bytePositions):
    minSteps = sys.maxsize
    queue = [(0, startPosition)]
    heapq.heapify(queue)
    visited = set()

    while len(queue) > 0:
        (steps, pos) = heapq.heappop(queue)
        if pos == endPosition:
            minSteps = min(minSteps, steps)
            break
        if pos in visited:
            continue
        visited.add(pos)

        for dir in directions:
            nextPos = (pos[0]+ dir[0], pos[1] + dir[1])
            if isInSideTheMap(nextPos) and nextPos not in bytePositions and nextPos not in visited:
                heapq.heappush(queue, (steps + 1, nextPos))
    return minSteps

if __name__ == "__main__":
    rows = 71
    cols = 71
    startPosition = (0,0)
    endPosition = (70,70)
    file = open("18/input.txt", "r")
    bytePositions = getInputs(file)
    minSteps = BFS(set(bytePositions[:1025]))
    print("Minimum number of steps needed to reach the exit", minSteps)
# solution 340
