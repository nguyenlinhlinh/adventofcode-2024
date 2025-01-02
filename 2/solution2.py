f= open("2/input.txt", "r")

matrix = []
INCREASING = 0
DECREASING = 1

for line in f:
    report = [int(i) for i in line.split()]
    matrix.append(report)

nbrOfSafeReports = 0

def checkReport(array):
    expect = None
    for i in range(len(array) - 1):
        diff = array[i] - array[i + 1]
        if abs(diff) == 0 or abs(diff) > 3:
            return False
        if expect == None:
            if diff < 0:
                expect = INCREASING
            else: 
                expect = DECREASING
        elif expect == INCREASING and diff > 0 or expect == DECREASING and diff < 0:
            return False 
    return True

for r in range(len(matrix)):
    for c in range(-1, len(matrix[r])):
        currArray = matrix[r][:]
        if c >= 0:
            currArray.pop(c)
        safe = checkReport(currArray)
        if safe == True:
            nbrOfSafeReports += 1
            break

print(nbrOfSafeReports)

#solution 717