occurences = 0
grid = []

with open("input.txt") as f:
    for line in f.read().splitlines():
        grid.append(list(line))

# search in each lines
for line in grid:
    line = "".join(line)
    occurences += line.count("XMAS")
    occurences += line.count("SAMX")

# search in each columns
for i in range(len(grid[0])):
    column = "".join([line[i] for line in grid])
    occurences += column.count("XMAS")
    occurences += column.count("SAMX")

# search in each top-left to bottom-right diagonals
for row in range(len(grid) - 3):
    for col in range(len(grid[0]) - 3):
        diagonal = "".join([grid[row + i][col + i] for i in range(4)])
        occurences += diagonal.count("XMAS")
        occurences += diagonal.count("SAMX")

# search in each top-right to bottom-left diagonals
for row in range(len(grid) - 3):
    for col in range(3, len(grid[0])):
        diagonal = "".join([grid[row + i][col - i] for i in range(4)])
        occurences += diagonal.count("XMAS")
        occurences += diagonal.count("SAMX")

print(occurences)
