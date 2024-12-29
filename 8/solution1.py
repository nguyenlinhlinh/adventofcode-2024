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
            antinodeA = (rA + rDis, cA + cDis)
            antinodeB = (rB - rDis, cB - cDis)
            if antinodeA[0] in range(rows) and antinodeA[1] in range(cols):
                antinodes.add(antinodeA)
            if antinodeB[0] in range(rows) and antinodeB[1] in range(cols):
                antinodes.add(antinodeB)

print(len(antinodes))

# solution 392
