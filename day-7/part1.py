data = []

with open("input.txt") as f:
    for line in f.read().splitlines():
        target, numbers = line.split(":")

        target = int(target)
        numbers = [int(n) for n in numbers[1:].split(" ")]

        data.append((target, numbers))

total_score = 0

for target, numbers in data:
    for i in range(2**(len(numbers) - 1)):
        score = numbers[0]

        for i, operation in enumerate(format(i, f"0{len(numbers) - 1}b")):
            if operation == "0":
                score += numbers[i + 1]
            elif operation == "1":
                score *= numbers[i + 1]

        if score == target:
            total_score += score
            break

print(total_score)
