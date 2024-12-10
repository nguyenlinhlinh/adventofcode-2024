import re

f= open("9/input.txt", "r")

input  = f.readline()

fileIdx = 0
result = []
emptySpace = 0
for i in range(len(input)):
    if i % 2 == 0:
        for j in range(int(input[i])):
            result.append((fileIdx, input[i]))
        fileIdx += 1
    else:
        for j in range(int(input[i])):
            result.append(".")
            emptySpace += 1

# move files to the left
left = 0
right = len(result) - 1

while left < right and emptySpace > 0:
    while result[left] != ".":
        left += 1
    while result[right] == "." and emptySpace > 0:
        right -= 1
    if left <= right:
        file = result.pop(right)
        result[left] = file
        emptySpace -= 1
    right = right - 1
    left += 1

checksum = 0
for position in range(len(result)):
    if result[position] == ".":
        continue
    checksum += position * result[position][0]
print(checksum)

# solution 6446899523367
