left_list = []
right_list = []

with open("input.txt") as f:
    for line in f:
        left, right = line.split("   ")
        right.replace("\n", "")

        left_list.append(int(left))
        right_list.append(int(right))

similarity_score = 0

for left in left_list:
    appearances = right_list.count(left)
    similarity_score += left * appearances

print(similarity_score)
