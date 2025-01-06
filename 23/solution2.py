from collections import defaultdict

# Solve by finding connected components using DFS

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

def DFS(node, connections, visited, table, idx):
    for neighbor in connections[node]:
        if neighbor not in visited:
            table[neighbor] = idx
            visited.add(neighbor)
            DFS(neighbor, connections, visited, table, idx)

def largestConnections(threeNodesConnections, connections):
    nodes = defaultdict(set)
    for (a, b, c) in threeNodesConnections:
        nodes[a].add(b)
        nodes[a].add(c)
        nodes[b].add(a)
        nodes[b].add(c)
        nodes[c].add(a)
        nodes[c].add(b)
    idx = 0
    table = {}
    visited = set()
    for n in nodes.keys():
        DFS(n, nodes, visited, table, idx)
        idx += 1
    groupByIdx = defaultdict(list)
    for k, v in table.items():
        groupByIdx[v].append(k)
    largest = []
    for (idx, group) in groupByIdx.items():
        allConnected = True
        for i in range(len(group)):
            for j in range(len(group)):
                if i == j:
                    continue
                if group[j] not in connections[group[i]]:
                    allConnected = False
        if allConnected and len(group) > len(largest):
            largest = group

    largest.sort()
    return largest

if __name__ == "__main__":
    file = open("23/input.txt", "r")
    connections = getInputs(file)
    sets = findConnections(connections)
    nodes = largestConnections(sets, connections)
    print(",".join(nodes))
    
# solution bg,bl,ch,fn,fv,gd,jn,kk,lk,pv,rr,tb,vw
