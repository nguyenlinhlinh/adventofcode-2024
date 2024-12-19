
# The idea is saving how many ways it could arrange the towels until startIdx and store it visited.
# When adding nextIdx to variances we need to also count how many way it could arrange the string to until startIdx to nextIdx.
import heapq

def getInputs(file):
    towels = {}
    patterns = []
    allTowels = file.readline().strip().split(",")
    for t in allTowels:
        t = t.strip()
        if t[0] in towels:
            towels[t[0]].append(t)
        else: 
            towels[t[0]] = [t]
    file.readline()
    for line in file:
        patterns.append(line.strip().replace('\n', ""))
    return (towels, patterns)

def isPossibleToBuildPattern(pattern, towels):
    print(pattern)
    length = len(pattern)
    variances = [0]
    heapq.heapify(variances)
    visited = {0:1}
    nbrOfways = 0
    while len(variances):
        startIdx = heapq.heappop(variances)
        char = pattern[startIdx]
        towelsStartWithChar = towels.get(char, [])
        for t in towelsStartWithChar:
            if len(t) > length - startIdx:
                continue
            if pattern[startIdx: startIdx + len(t)] == t: 
                nextIdx = startIdx + len(t)
                if nextIdx == length:
                    nbrOfways += visited[startIdx]
                    continue
                if nextIdx < length:
                    if nextIdx not in visited:
                        heapq.heappush(variances, nextIdx)
                        visited[nextIdx] = visited[startIdx]
                    else:
                        visited[nextIdx] += visited[startIdx]
    return nbrOfways

if __name__ == "__main__":
    file = open("19/input.txt", "r")
    (towels, patterns) = getInputs(file)
    count = 0
    for pattern in patterns:
        nbrOfways = isPossibleToBuildPattern(pattern, towels)
        count += nbrOfways
    print("nbr of ways", count)

# solution 777669668613191
