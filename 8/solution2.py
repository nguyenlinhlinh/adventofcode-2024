import re

f= open("8/input.txt", "r")

input  = {}

rows = 0
cols = 0
for line in f:
    cols = 0
    for char in line.strip():
        if char != ".":
            if char in input:
                input[char].append((rows, cols))
            else:
                input[char] = [(rows, cols)]
        cols += 1
    rows += 1

antinodes = set()
for antenna, points in input.items():
    for pointA in points:
        (rA, cA) = pointA 
        for pointB in points:
            if pointA == pointB:
                continue
            (rB, cB) = pointB
            rDis = rA - rB
            cDis = cA - cB
            currPosA = (rA + rDis, cA + cDis)
            while currPosA[0] in range(rows) and currPosA[1] in range(cols):
                antinodes.add(currPosA)
                (r, c) = currPosA
                currPosA = (r + rDis, c + cDis)
            currPosB = (rB + rDis, cB + cDis)
            while currPosB[0] in range(rows) and currPosB[1] in range(cols):
                antinodes.add(currPosB)
                (r, c) = currPosB
                currPosB = (r - rDis, c - cDis)

print(len(antinodes))

# solution 1235
