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
    return (rows, cols, startPosition, endPosition, allowedPositions)

# Use BFS to find shortest paths. 
# To find multiple shortest paths the important things must be what to store in visited list. 
# In this case not just the position but also the direction when being at that position.
def BFS(startPosition, endPosition, allowedPositions):
    bestTiles = set()
    queue = [(0, startPosition, EAST, set([startPosition]))]
    heapq.heapify(queue) # sort by score
    visited = set()
    minScore = sys.maxsize
    while len(queue) > 0:
        (score, pos, dir, path) = heapq.heappop(queue)
        if pos == endPosition and score <= minScore:
            bestTiles = bestTiles.union(path)
            minScore = min(minScore, score)
            continue
        visited.add((pos, dir))
        if score + 1 > minScore:
            continue
        #Same direction
        nextPos = (pos[0] + dir[0], pos[1] + dir[1]) 
        if nextPos in allowedPositions and (nextPos, dir) not in visited:
            nextPath = path.copy()
            nextPath.add(nextPos)
            heapq.heappush(queue, (score + 1, nextPos, dir, nextPath))

        (x,y) = dir 
        # Rotate 90 clockwise
        clockwise = (y, -x) 
        if (pos, clockwise) not in visited:
            heapq.heappush(queue, (score + 1000, pos, clockwise, path.copy()))
        # Rotate 90 counterclockwise
        counterwise = (-y, x) 
        if (pos, counterwise) not in visited:
            heapq.heappush(queue, (score + 1000, pos, counterwise, path.copy()))
    return bestTiles

if __name__ == "__main__":
    file= open("16/input.txt", "r")
    (rows, cols, startPosition, endPosition, allowedPositions) = getInputs(file)
    bestTiles = BFS(startPosition, endPosition, allowedPositions)
    print("number of tiles", len(bestTiles))

# solution 554
