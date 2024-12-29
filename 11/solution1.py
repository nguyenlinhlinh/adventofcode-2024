f= open("11/input.txt", "r")

input = f.readline().strip().split(" ")
stones = {}
for i in input:
    stones[i] = 1

for blink in range(24, -1, -1):
    next = {}
    for stone, count in stones.items():
        nbr = int(stone)
        left, right = None, None

        if stone == '0':
            left = '1'
        elif len(stone) % 2 == 0:
            mid = int(len(stone) / 2)
            left = str(int(stone[: mid]))
            right = str(int(stone[mid:]))
        else:
            newNbr = nbr * 2024
            left = str(newNbr)
        
        if left in next:
            next[left] += count
        else: 
            next[left] = count
        if right:
            if right in next:
                next[right] += count
            else:
                next[right] = count
    stones = next
        
print("total", sum(stones.values()))
# solution 203953
