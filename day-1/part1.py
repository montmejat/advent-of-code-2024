left_list = []
right_list = []

with open("input.txt") as f:
    for line in f:
        left, right = line.split("   ")
        right.replace("\n", "")

        left_list.append(int(left))
        right_list.append(int(right))

left_list.sort()
right_list.sort()

distance = 0

for left, right in zip(left_list, right_list):
    distance += abs(left - right)

print(distance)
