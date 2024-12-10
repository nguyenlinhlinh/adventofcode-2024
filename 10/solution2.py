# Solved by using BFS without visited list. 


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

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
directions = [UP, DOWN, LEFT, RIGHT]


total = 0
for startPos in startPositions:
    queue = [startPos]
    ratingCounter = 0
    while len(queue) > 0:
        pos = queue.pop(0)
        (r, c) = pos
        height = matrix[r][c]
        for dir in directions:
            (nR, nC) = (r + dir[0], c+ dir[1])
            if not (nR in range(rows) and nC in range(cols)):
                continue
            nHeight = matrix[nR][nC]
            if nHeight - height != 1:
                continue
            if nHeight == 9:
                ratingCounter += 1
            else:
                queue.append((nR, nC))
    total += ratingCounter 
       
print(total)
# solution 1794
