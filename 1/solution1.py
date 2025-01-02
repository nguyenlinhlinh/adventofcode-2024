f= open("1/input.txt", "r")

list1 = []
list2 = []

for line in f:
    [a, b] = line.split()
    list1.append(int(a))
    list2.append(int(b))

list1.sort()
list2.sort()

total = 0
for i in range(len(list1)):
    total += abs(list1[i] - list2[i])

print("total distance", total)