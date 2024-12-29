import sys
f= open("16/input.txt", "r")

WALL = '#'
EMPTY = '.'
NORTH = (-1, 0)
SOUTH = (1, 0)
WEST = (0, -1)
EAST = (0, 1)
startPosition = None
endPosition = None
path = set()
directions = []
rows = 0
cols = 0

# DIRECTION = {UP: "up", DOWN: "down", LEFT: "left", RIGHT: "right"}

for line in f:
    line = line.strip().replace('\n', "")
    cols = len(line)
    for c in range(len(line)):
        char = line[c]
        if char == 'S':
            startPosition = (rows, c)
        if char == 'E':
            endPosition = (rows, c)
        if char != '#':
            path.add((rows, c))
    rows += 1


def printMatrix(start, end):
    matrix = [["#" for c in range(cols)] for r in range(rows) ]
    for (r,c) in path:
        matrix[r][c] = '.'

    matrix[start[0]][start[1]] = 'S'
    matrix[end[0]][end[1]] = 'E'
    for array in matrix:
        print("".join(array))

def isInSideTheMap(pos):
    return pos[0] in range(rows) and pos[1] in range(cols)

def BFS():
    minScore = sys.maxsize
    queue = [(startPosition, EAST, 0, [startPosition])]
    visited = set()
    counter = 0
    while len(queue) > 0:
        # print(queue)
        queue.sort(key=lambda e:e[2])
        (pos, dir, point, path) = queue.pop(0)
        if pos == endPosition:
            minScore = min(minScore, point)
            print("minScore", minScore)
            continue
        if (pos, dir) in visited:
            continue
        visited.add((pos, dir))
        #Same direction
        nextPos = (pos[0] + dir[0], pos[1] + dir[1])
        if nextPos == endPosition:
            print("end pos", point)
        if nextPos in path and (nextPos, dir) not in visited:
            queue.append((nextPos, dir, point + 1, path.append(nextPos)))

        (x,y) = dir 
        # Rotate 90 clockwise
        clockwise = (y, -x)
        if (point + 1000) > minScore:
            continue
        if (pos, clockwise) not in visited:
            queue.append((pos, clockwise, point + 1000, path.append()))
        # Rotate 90 counterwise
        counterwise = (-y, x)
        if (pos, counterwise) not in visited:
            queue.append((pos, counterwise, point + 1000))
        counter += 1
    print(minScore)

if __name__ == "__main__":
    # printMatrix(startPosition, endPosition)
    BFS()
    # print("total", total)
# solution 103512
