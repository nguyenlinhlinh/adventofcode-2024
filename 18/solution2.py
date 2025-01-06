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

def isInSideTheMap(pos, size):
    return pos[0] in range(size) and pos[1] in range(size)

def BFS(bytePositions, size):
    queue = [(0, startPosition)]
    heapq.heapify(queue)
    visited = set()
    
    while len(queue) > 0:
        (point, pos) = heapq.heappop(queue)
        if pos == endPosition:
            return True
        if pos in visited:
            continue
        visited.add(pos)
        for dir in directions:
            nextPos = (pos[0]+ dir[0], pos[1] + dir[1])
            if isInSideTheMap(nextPos, size) and nextPos not in bytePositions and nextPos not in visited:
                heapq.heappush(queue,(point + 1, nextPos))
    return False


if __name__ == "__main__":
    file = open("18/input.txt", "r")
    bytePositions = getInputs(file)
    startPosition = (0,0)
    endPosition = (70,70)
    size = 71
    for i in range(len(bytePositions)-1, -1, -1): # Iterate from the end of the list since there must be many bytes to block the path.
        found = BFS(set(bytePositions[:i]), size)
        if found == True:
            print("Coordinates of the first byte that will prevent the exit from being reachable",i, bytePositions[i])
            break

# solution 34,32
