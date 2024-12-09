lab_map = []
visited = set()
direction = "up"

with open("input.txt") as f:
    for i, line in enumerate(f.read().splitlines()):
        lab_map.append(list(line))

        if "^" in line:
            col = line.find("^")
            row = i

visited.add((row, col))

rows = len(lab_map)
cols = len(lab_map[0])

while True:
    if direction == "up":
        next_row = row - 1
        next_col = col
    elif direction == "down":
        next_row = row + 1
        next_col = col
    elif direction == "left":
        next_row = row
        next_col = col - 1
    elif direction == "right":
        next_row = row
        next_col = col + 1

    if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
        break

    if lab_map[next_row][next_col] == "#":
        if direction == "up":
            direction = "right"
        elif direction == "right":
            direction = "down"
        elif direction == "down":
            direction = "left"
        elif direction == "left":
            direction = "up"
    else:
        row = next_row
        col = next_col
        visited.add((row, col))

print(len(visited))
