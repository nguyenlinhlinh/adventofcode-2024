

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

def isInsideGarden(pos):
    (r, c) = pos
    return r in range(len(garden)) and c in range(len(garden[0]))

def getRegions(garden):
    regions = []
    visited = set()
    for r in range(len(garden)):
        for c in range(len(garden[0])):
            if (r,c) in visited:
                continue
            queue = [(r, c)]
            plot = garden[r][c]
            area = 0
            perimeters = 0
            while len(queue):
                (cR, cC) = queue.pop()
                if (cR, cC) in visited or garden[cR][cC] != plot:
                    continue
                visited.add((cR, cC))
                area += 1
                for dir in DIRECTIONS:
                    nextPos = (cR + dir[0], cC + dir[1])
                    if not isInsideGarden(nextPos) or garden[nextPos[0]][nextPos[1]] != plot:
                        perimeters += 1
                        continue
                    if isInsideGarden(nextPos) and garden[nextPos[0]][nextPos[1]] == plot and not nextPos in visited:
                        queue.append(nextPos)
            regions.append((plot, area, perimeters))
    return regions
if __name__ == "__main__":
    file = open("12/input.txt", "r")
    garden = getInputs(file)
    regions = getRegions(garden)

    print("total price of fencing all regions", sum([area * perimeter for (plot, area, perimeter) in regions]))
# solution 1549354
