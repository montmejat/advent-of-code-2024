import re

sum = 0

with open("input.txt") as f:
    for line in f.read().splitlines():
        multiplies = re.findall(r"mul\(\d+,\d+\)", line)
        for multiply in multiplies:
            a, b = map(int, re.findall(r"\d+", multiply))
            sum += a * b

print(sum)
