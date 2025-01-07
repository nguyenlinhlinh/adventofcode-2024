import heapq
import sys
from collections import defaultdict

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
directions = [UP, DOWN, LEFT, RIGHT]

def getInputs(file):
    walls = set()
    tracks = set()
    startPosition = None
    endPosition = None
    rows = 0
    cols = 0
    for line in file:
        line = line.strip()
        cols = 0
        for char in line:
            if char == 'S':
                tracks.add((rows, cols)) 
                startPosition = (rows, cols)
            if char == 'E':
                tracks.add((rows, cols)) 
                endPosition = (rows, cols)
            if char == '#':
                walls.add((rows, cols)) 
            if char == '.':
                tracks.add((rows, cols)) 
            cols += 1
        rows+= 1
    return (startPosition, endPosition, walls, tracks, rows, cols)

def isInsideMap(pos, rows, cols):
    return pos[0] in range(rows) and pos[1] in range(cols)

def Dijkstra(source, tracks):
    distances = {}
    prev = {}
    distances[source] = 0
    queue = [(0, source)]
    heapq.heapify(queue)
    for pos in tracks:
        if pos != source:
            distances[pos] = sys.maxsize
            prev[pos] = None
    while len(queue):
        (dist, (r,c)) = heapq.heappop(queue)
        for (dR, dC) in directions:
            nextPos = (r + dR, c + dC)
            if nextPos in tracks:
                distance = distances[(r,c)] + 1
                if distance < distances[nextPos]:
                    distances[nextPos] = distance
                    prev[nextPos] = pos
                    heapq.heappush(queue, (distance, nextPos))
    return distances

def countCheats(distancesFromStart, distancesFromEnd, timeWithoutCheat, minTimeSaved):
    cheats = defaultdict(int)
    visited = set()
    count = 0
    for wall in walls:
        for dir in directions:
            start = (wall[0] + dir [0], wall[1]+ dir[1])
            end = (wall[0] + dir [0] * -1, wall[1]+ dir[1] * -1)
            if (start, end) in visited:
                continue
            visited.add((start, end))
            if isInsideMap(start, rows, cols) and isInsideMap(end, rows, cols) and start not in walls and end not in walls:
                time = distancesFromStart[start]  + 2 + distancesFromEnd[end]
                if timeWithoutCheat - time >= minTimeSaved:
                    cheats[timeWithoutCheat - time] += 1
                count += 1
    return cheats

if __name__ == "__main__":
    file = open("20/input.txt", "r")
    (startPosition, endPosition, walls, tracks, rows, cols) = getInputs(file)
    distancesFromStart = Dijkstra(startPosition, tracks)
    distancesFromEnd = Dijkstra(endPosition, tracks)
    cheats = countCheats(distancesFromStart, distancesFromEnd, distancesFromEnd[startPosition], 100)
    print("How many cheats would save you at least 100 picoseconds? ", sum([v for v in cheats.values()]))
# solution 1293
