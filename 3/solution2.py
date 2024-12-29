import re

f= open("3/input.txt", "r")
text = f.read()
operations = re.findall(r'do\(\)|don\'t\(\)|mul\(\d+,\d+\)', text)
total = 0
enabled = True
for op in operations:
    if op == "don't()":
        enabled = False
    elif op == "do()":
        enabled = True
    elif op.startswith("mul"):
        if enabled:
            r = re.findall(r'\d+,\d+', op)
            [a, b] = r[0].split(",")
            total += int(a) * int(b)
print(total)

# solution 111762583