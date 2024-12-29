import sys
import heapq

EAST = (0, 1)

def getInputs(file):
    startPosition, endPosition = None, None
    allowedPositions = set()
    rows, cols = 0, 0
    for line in file:
        line = line.strip().replace('\n', "")
        cols = len(line)
        for c in range(len(line)):
            char = line[c]
            if char == 'S':
                startPosition = (rows, c)
            if char == 'E':
                endPosition = (rows, c)
            if char != '#':
                allowedPositions.add((rows, c))
        rows += 1
    return (startPosition, endPosition, allowedPositions)

def BFS(startPosition, endPosition, allowedPositions):
    minScore = sys.maxsize
    queue = [(0, startPosition, EAST)]
    heapq.heapify(queue)
    visited = set()
    while len(queue) > 0:
        (point, pos, dir) = heapq.heappop(queue)
        if pos == endPosition:
            minScore = min(minScore, point)
            continue
        if (pos, dir) in visited:
            continue
        visited.add((pos, dir))
        #Same direction
        nextPos = (pos[0] + dir[0], pos[1] + dir[1])
        if nextPos in allowedPositions and (nextPos, dir) not in visited:
            heapq.heappush(queue, (point + 1, nextPos, dir))

        if (point + 1000) > minScore:
            continue
        (x,y) = dir 
        # Rotate 90 clockwise
        clockwise = (y, -x)
        if (pos, clockwise) not in visited:
            heapq.heappush(queue, (point + 1000, pos, clockwise))
        # Rotate 90 counterwise
        counterwise = (-y, x)
        if (pos, counterwise) not in visited:
            heapq.heappush(queue, (point + 1000, pos, counterwise))
    return minScore

if __name__ == "__main__":
    file = open("16/input.txt", "r")
    (startPosition, endPosition, allowedPositions) = getInputs(file)
    minScore = BFS(startPosition, endPosition, allowedPositions)
    print("minScore", minScore)
# solution 103512
