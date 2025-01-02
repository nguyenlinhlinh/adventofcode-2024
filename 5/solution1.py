f= open("5/input.txt", "r")

rules = {}
orders = []
total = 0
for line in f:
    if "|" in line:
        [a, b] = line.strip().split("|")
        if int(a) in rules:
            rules[int(a)].append(int(b))
        else: 
            rules[int(a)] = [int(b)]
    elif line == "\n":
        continue
    else:
        order = line.strip().split(",")
        orders.append([int(i) for i in order])

for order in orders:
    exist = set()
    correctOrder = True
    for nbr in order:
        if nbr in rules:
            rule = rules[nbr]
            for r in rule:
                if r in exist:
                    correctOrder = False
                    break
            if correctOrder == False:
                break
        exist.add(nbr)
    if correctOrder == True:
        middlePage = order[int(len(order)/2)]
        total += middlePage

print(total)
# solution 6949
