from collections import defaultdict
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

def getInputs(file):
    garden = []
    for line in file:
        line = line.strip()
        garden.append([char for  char in line])
    return garden

def findVerticalSides(perimeter):
    verticalMap = {}
    sides = []
    for i in range(len(perimeter)):
        (r, c) = perimeter[i]
        if c in verticalMap:
            verticalMap[c].append(r)
        else:
            verticalMap[c] = [r] 
    
    for c, array in verticalMap.items():
        array.sort()
        curr = 0
        for i in range(len(array)):
            if i == len(array) - 1 or array[i + 1] - array[i] != 1 :
                if (i + 1 - curr) > 1:
                    sides.append([(r, c) for r in array[curr: i + 1]])
                curr = i + 1
    return sides

def findHorisontalSides(perimeter):
    sides = []
    horisontelMap = {}
    for i in range(len(perimeter)):
        (r, c) = perimeter[i]
        if r in horisontelMap:
            horisontelMap[r].append(c)
        else:
            horisontelMap[r] = [c] 
    for r, array in horisontelMap.items():
        array.sort()
        curr = 0
        for i in range(len(array)):
            if i == len(array) -1 or array[i + 1] - array[i] != 1:
                if (i + 1 - curr) > 1:
                    sides.append([(r, c) for c in array[curr: i + 1]])
                curr = i + 1
    return sides

def getPerimetersForEdges(perimeters, edge, directions):
    result = []
    for pos in edge:
        (r, c) = pos
        for dir in directions:
            p = (r + dir[0], c + dir[1])
            if p in perimeters:
                result.append(p)
    return result

def calcSides(perimeters, regions):
    edges = []
    count = sum(perimeters.values())
    for point in regions:
        (r, c) = point
        if (r + 1, c) in perimeters or (r - 1, c) in perimeters or (r, c - 1) in perimeters or (r, c + 1) in perimeters:
            edges.append((r, c))

    verticalEdges = findVerticalSides(edges)
    horisontalEdges = findHorisontalSides(edges)
    sides = []
    for edge in horisontalEdges:
        horizontalPerimeters = getPerimetersForEdges(perimeters, edge, [UP, DOWN])
        sides += findHorisontalSides(horizontalPerimeters)
    for edge in verticalEdges:
        verticalPerimeters = getPerimetersForEdges(perimeters, edge, [LEFT, RIGHT])
        sides += findVerticalSides(verticalPerimeters)
    for arrayPer in sides:
        count -= (len(arrayPer) - 1)

    return count

def isInsideGarden(pos):
    (r, c) = pos
    return r in range(len(garden)) and c in range(len(garden[0]))

def getRegions(garden):
    visited = set()
    regions = []
    for r in range(len(garden)):
        for c in range(len(garden[0])):
            if (r,c) in visited:
                continue
            queue = [(r, c)]
            plot = garden[r][c]
            region = []
            area = 0
            perimeters = defaultdict(int)
            while len(queue):
                (cR, cC) = queue.pop()
                if (cR, cC) in visited or garden[cR][cC] != plot:
                    continue
                visited.add((cR, cC))
                area += 1
                region.append((cR, cC))
                for dir in DIRECTIONS:
                    nextPos = (cR + dir[0], cC + dir[1])
                    if not isInsideGarden(nextPos) or garden[nextPos[0]][nextPos[1]] != plot:
                        perimeters[nextPos] += 1
                        continue
                    if isInsideGarden(nextPos) and garden[nextPos[0]][nextPos[1]] == plot and not nextPos in visited:
                        queue.append(nextPos)
            sides = calcSides(perimeters, region)
            regions.append((plot, area, sides))
    return regions

if __name__ == "__main__":
    file = open("12/input.txt", "r")
    garden = getInputs(file)
    regions = getRegions(garden)
    print("total price of fencing all regions", sum([area * sides for (plot, area, sides) in regions]))
# solution 937032
