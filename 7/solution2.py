import re

f= open("7/input.txt", "r")

inputs  = []

for line in f:
    [value, numbers] = line.strip().split(":")
    inputs.append((int(value), [int(n) for n in numbers.strip().split(" ")]))

def isPossible(numbers, testValue):
    queue = [numbers[0]] 
    for i in range(1, len(numbers)):
        nextValues = []
        nbr = numbers[i]
        for value in queue:
            # * or + or || 
            result = [value * nbr, value + nbr, int(str(value) + str(nbr))]
            for r in result:
                if r <= testValue:
                    nextValues.append(r)
        queue = nextValues
    for v in queue:
        if v == testValue:
            return True
    return False


total = 0
   
for (value, numbers) in inputs:
    if isPossible(numbers, value):
        total += value        

print(total)

# solution 438027111276610
