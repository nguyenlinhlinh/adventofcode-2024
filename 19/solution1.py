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
    length = len(pattern)
    variances = [0]
    visited = set()
    while len(variances):
        startIdx = variances.pop()
        char = pattern[startIdx]
        towelsStartWithChar = towels.get(char, [])
        for t in towelsStartWithChar:
            if len(t) > length - startIdx:
                continue
            if pattern[startIdx: startIdx + len(t)] == t: 
                restIdx = startIdx + len(t)
                if restIdx == length:
                    return True                
                
                if restIdx not in visited:                    
                    variances.append(restIdx)
                    visited.add(restIdx)
    return False

if __name__ == "__main__":
    file = open("19/input.txt", "r")
    (towels, patterns) = getInputs(file)
    count = 0
    for pattern in patterns:
        possible = isPossibleToBuildPattern(pattern, towels)
        if possible:
            count += 1
    print("count", count)

# solution 209
