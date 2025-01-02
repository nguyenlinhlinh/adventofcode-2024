f= open("2/input.txt", "r")

matrix = []
INCREASING = 0
DECREASING = 1

for line in f:
    report = [int(i) for i in line.split()]
    matrix.append(report)

nbrOfSafeReports = 0
for r in range(len(matrix)):
    expect = None
    safe = True
    for c in range(0, len(matrix[r]) -1):
        diff = matrix[r][c] - matrix[r][c + 1]
        if abs(diff) == 0 or abs(diff) > 3:
            safe = False
            break
        if expect == None:
            if diff < 0:
                expect = INCREASING
            else: 
                expect = DECREASING
        elif expect == INCREASING and diff > 0 or expect == DECREASING and diff < 0:
            safe = False 
            break
    if safe:
        nbrOfSafeReports += 1

print("Number of safe reports", nbrOfSafeReports)

# solution 686