import re

f= open("4/input.txt", "r")

matrix = []

for line in f:
    array = [c for c in line if c != "\n"]
    matrix.append(array)

rows = len(matrix)
cols = len(matrix[0])

total = 0
xmas = ["XMAS", "SAMX"]

for r in range(rows):
    for c in range(cols):
        array = []
        if c + 3 < cols: 
            horisontal = matrix[r][c] + matrix[r][c + 1] + matrix[r][c + 2] + matrix[r][c+3]
            array += [horisontal]
        if r + 3 < rows:
            vertical = matrix [r][c] + matrix[r+1][c] + matrix[r+2][c] + matrix[r+3][c]
            array += [vertical]
        if r + 3 < rows and c + 3 < cols:
            ltrDiagonal = matrix[r][c] + matrix[r+1][c + 1] + matrix[r + 2][c + 2] + matrix[r + 3][c + 3]
            rtlDiagonal = matrix[r][c + 3] + matrix[r+1][c+ 2] + matrix[r + 2][c + 1] + matrix[r+ 3][c]
            array += [ltrDiagonal, rtlDiagonal]

        for w in array:
            if w in xmas:
                total += 1

print(total)
# solution 2500
