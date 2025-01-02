# Solved using sliding window

f= open("4/input-simple.txt", "r")

matrix = []
for line in f:
    array = [c for c in line if c != "\n"]
    matrix.append(array)

rows = len(matrix)
cols = len(matrix[0])

total = 0
window = []
mas = ["MAS", "SAM"]
for r in range(rows - 2):
    window = [matrix[i] for i in range(r, r + 3)]
    for i in range(cols - 2):
        ltrDiagonal = matrix[r][i] + matrix[r+1][i+1] + matrix[r+ 2][i + 2]
        rtlDiagonal = matrix[r][i+2] + matrix[r+1][i+1] + matrix[r+2][i]
        if ltrDiagonal in mas and rtlDiagonal in mas:
            total += 1



print(total)
# solution 1933
