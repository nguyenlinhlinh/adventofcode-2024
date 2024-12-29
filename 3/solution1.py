import re

f= open("3/input.txt", "r")

text = f.read()
operations = re.findall(r'mul\((\d+,\d+)\)', text)
total = 0
for op in operations:
    [a, b] = op.split(",")
    total += int(a) * int(b)

print(total)
# solution 169021493
