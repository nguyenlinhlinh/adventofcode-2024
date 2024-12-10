# Solved by using BFS with visited list
f= open("10/input.txt", "r")

matrix = []
startPositions = []
rows = 0
cols = 0
for line in f:
    line = line.strip()
    array = []
    cols = 0
    for char in line:
        if char == '0':
            startPositions.append((rows, cols))
        array.append(int(char)) 
        cols += 1
    matrix.append(array)
    rows+= 1

total = 0
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
directions = [UP, DOWN, LEFT, RIGHT]

for startPos in startPositions:
    queue = [startPos]
    visited = set()
    score = 0
    while len(queue) > 0:
        pos = queue.pop(0)
        if pos in visited:
            continue
        visited.add(pos)
        (r, c) = pos
        height = matrix[r][c]
        if height == 9:
            score += 1
            continue
        for dir in directions:
            (nR, nC) = (r + dir[0], c+ dir[1])
            if nR in range(rows) and nC in range(cols):
                nHeight = matrix[nR][nC]
                if nHeight - height == 1 and not (nR, nC) in visited:
                    queue.append((nR, nC))
    total += score
        
print(total)
# solution 811
