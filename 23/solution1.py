from collections import defaultdict

def getInputs(file):
    connections = defaultdict(list)
    for line in file.readlines():
        a, b = line.strip().replace("\n", "").split("-")
        connections[a].append(b)
        connections[b].append(a)
    return connections

def findConnections(connections):
    threeNodes = set()
    for a in connections:
        neighbors = connections[a]
        for i in range(len(neighbors)):
            for j in range(len(neighbors)):
                if i == j:
                    continue
                b = neighbors[i]
                c = neighbors[j]
                com = [a, b, c]
                com.sort()
                if c in connections[b] and b in connections[c]:
                    if a.startswith('t') or b.startswith('t') or c.startswith('t'):
                        threeNodes.add(tuple(com))
    return threeNodes

if __name__ == "__main__":
    file = open("23/input.txt", "r")
    connections = getInputs(file)
    sets = findConnections(connections)
    print(len(sets))
    
# solution 1238
