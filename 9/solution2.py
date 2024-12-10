# Optimised by not store result in an common array for both space and file but store them separately and also remove empty space size 0 from emptySpace array. 
f= open("9/input.txt", "r")

input  = f.readline().strip()

fileIdx = 0
emptySpace = []
files = []
startIdx = 0

for i in range(len(input)):
    size = int(input[i])
    if i % 2 == 0:
        files.append((fileIdx, startIdx, size))
        fileIdx += 1
    else:
        if size > 0:
            emptySpace.append((size, startIdx))
    startIdx += size


for index in range(len(files)-1, -1, -1):
    (fileIdx, fileStartIdx, fileSize) = files[index]
    fileEndIdx = fileStartIdx + fileSize - 1
    for i in range(len(emptySpace)):
        (spaceSize, spaceStartIdx) = emptySpace[i]
        if fileSize <= spaceSize:
            if spaceStartIdx + fileSize > fileEndIdx:
                break
            files[index] = (fileIdx, spaceStartIdx, fileSize)
            newSize = spaceSize - fileSize
            if newSize <= 0:
                emptySpace.pop(i)
            else:
                spaceEndIdx = spaceStartIdx + fileSize
                emptySpace[i] = (newSize, spaceEndIdx)
            break

checksum = 0
for (fileIdx, startIdx, size) in files:
    for position in range(startIdx, startIdx + size):
        checksum += position * fileIdx

print(checksum)

# solution 6478232739671