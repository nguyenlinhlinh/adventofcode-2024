import heapq
import sys
from collections import defaultdict
def getInputs(file):
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
                startPosition = (rows, cols)
                tracks.add((rows, cols)) 
            if char == 'E':
                endPosition = (rows, cols)
                tracks.add((rows, cols)) 
            if char == '.':
                tracks.add((rows, cols)) 
            cols += 1
        rows+= 1
    return (startPosition, endPosition, tracks, rows, cols)

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
directions = [UP, DOWN, LEFT, RIGHT]

def isInsideMap(pos, rows, cols):
    return pos[0]in range(rows) and pos[1] in range(cols)

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

def countCheats(distancesFromStart, distancesFromEnd, tracks, timeWithoutCheat, maxCheats, minTimeSaved):
    cheats = defaultdict(int)
    visited = set()
    count = 0
    for start in tracks:
        for r in range(max(0, start[0] - (maxCheats + 1)), min(rows, start[0] + (maxCheats +1))):
            for c in range(max(0, (start[1] - (maxCheats)) + abs(r - start[0])), min(rows, (start[1] + (maxCheats + 1)) - abs(r - start[0]))):
                end = (r, c)
                if end in tracks and start != end and (start, end) not in visited:
                    manhattanDis = abs(end[0] - start[0]) + abs(end[1] - start[1])
                    if manhattanDis > maxCheats:
                        continue
                    visited.add((start, end))
                    time = distancesFromStart[start] + manhattanDis + distancesFromEnd[end]
                    if timeWithoutCheat - time >= minTimeSaved:
                        cheats[timeWithoutCheat - time] += 1
                        count += 1
    return cheats


if __name__ == "__main__":
    file = open("20/input.txt", "r")
    (startPosition, endPosition, tracks, rows, cols) = getInputs(file)
    distancesFromStart = Dijkstra(startPosition, tracks)
    distancesFromEnd = Dijkstra(endPosition, tracks)
    cheats = countCheats(distancesFromStart, distancesFromEnd, tracks, distancesFromStart[endPosition], 20, 100)
    print("How many cheats would save you at least 100 picoseconds?", sum([v for v in cheats.values()]))
    # Currently take 6.28s to finish. Could it be that python is slow or my solution is not optimised enough.
# solution #977747
