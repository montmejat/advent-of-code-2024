import re

sum = 0
process = True

with open("input.txt") as f:
    for line in f.read().splitlines():
        multiplies = re.findall(r"(mul\(\d+,\d+\)|do\(\)|don\'t\(\))", line)

        for multiply in multiplies:
            if multiply == "do()":
                process = True
                continue
            elif multiply == "don't()":
                process = False
                continue

            if process:
                a, b = map(int, re.findall(r"\d+", multiply))
                sum += a * b

print(sum)
