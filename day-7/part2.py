from tqdm import tqdm

def ternary(n, fill):
    if n == 0:
        return '0' * fill

    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))

    ternary_value = ''.join(reversed(nums))
    return ternary_value.zfill(fill)


data = []

with open("input.txt") as f:
    for line in f.read().splitlines():
        target, numbers = line.split(":")

        target = int(target)
        numbers = [int(n) for n in numbers[1:].split(" ")]

        data.append((target, numbers))

total_score = 0

for target, numbers in tqdm(data):
    for i in range(3**(len(numbers) - 1)):
        score = numbers[0]

        for j, operation in enumerate(ternary(i, len(numbers) - 1)):
            if operation == "0":
                score += numbers[j + 1]
            elif operation == "1":
                score *= numbers[j + 1]
            elif operation == "2":
                score = int(f"{score}{numbers[j + 1]}")

        if score == target:
            total_score += score
            break

print(total_score)
