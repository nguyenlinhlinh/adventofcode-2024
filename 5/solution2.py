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

incorrectOrders = []
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
    if correctOrder == False:
        incorrectOrders.append(order)

# Solve by reordering all numbers before current last number in newOrders until getting correct order

for order in incorrectOrders:
    exist = set()
    newOrder = []
    for nbr in order:
        newOrder.append(nbr)
        correct = False
        while not correct:
            updated = False
            lastNbr = newOrder[-1]
            if lastNbr in rules:
                rule = rules[lastNbr]
                for i in range(len(newOrder)-1 , -1, -1):
                    page = newOrder[i]
                    if page in rule:
                        newOrder.pop(i)
                        newOrder.append(page)
                        updated = True
            if updated == False:
                correct = True
    middlePage = newOrder[int(len(order)/2)]
    total += middlePage

print(total)
# solution 4145
