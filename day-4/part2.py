occurences = 0
grid = []

with open("input.txt") as f:
    for line in f.read().splitlines():
        grid.append(list(line))

words = ["SAM", "MAS"]

# search crosses
for row in range(len(grid) - 2):
    for col in range(len(grid[0]) - 2):
        diag1 = "".join([grid[row + i][col + i] for i in range(3)])
        diag2 = "".join([grid[row + i][col + 2 - i] for i in range(3)])

        if diag1 in words and diag2 in words:
            occurences += 1

print(occurences)
