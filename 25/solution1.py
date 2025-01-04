def getInputs(file, rows):
    locks = []
    keys = []
    current = []
    isFirstRow = True
    lock = ''
    count = 0
    for line in file.readlines():
        if line == '\n':
            continue
        line = line.strip().replace("\n", "")
        if isFirstRow:
            isFirstRow = False
            current = [ 0 for i in range(len(line))]
            lock = line[0]
        for i in range(len(line)):
            if line[i] == lock:
                current[i] += 1
        if count == rows:
            if lock == '#':
                locks.append(tuple(current))
            else:
                keys.append(tuple([rows - 1 - n for n in current]))
            isFirstRow = True
            count = 0
            continue
        count += 1
        
    return (locks, keys)

def findUniqueLockKeyPairs(locks, keys, rows):
    pairs = set()
    for lock in locks:
        for key in keys:
            fit = True
            for i in range(len(lock)):
                if lock[i] + key[i] > rows - 1:
                    fit = False
                    break
            if fit:
                pairs.add((lock, key))
    return pairs
if __name__ == "__main__":
    file = open("25/input.txt", "r")
    (locks, keys) = getInputs(file, 6)
    pairs = findUniqueLockKeyPairs(locks, keys, 6)
    print(len(pairs))    
# solution 3451
