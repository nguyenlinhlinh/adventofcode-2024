f= open("1/input.txt", "r")

list1 = []
list2 = []

for line in f:
    [a, b] = line.split()
    list1.append(int(a))
    list2.append(int(b))

memo = {}
total = 0

for i in range(len(list2)):
    b = list2[i]
    if b in memo:
        memo[b] += 1
    else:
        memo[b] = 1

for i in range(len(list1)):
    a = list1[i]
    c  = 0
    if a in memo:
        c = memo[a]
    total += a * c

print("total similarity score", total)

# solution 23981443