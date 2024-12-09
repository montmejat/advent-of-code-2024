lab_map = []

with open("input.txt") as f:
    for i, line in enumerate(f.read().splitlines()):
        lab_map.append(list(line))

        if "^" in line:
            start_col = line.find("^")
            start_row = i

rows = len(lab_map)
cols = len(lab_map[0])

loops = 0

for obs_row in range(rows):
    for obs_col in range(cols):
        if lab_map[obs_row][obs_col] != ".":
            continue

        print(f"{(obs_row * cols) + obs_col}/{rows * cols}")

        lab_map[obs_row][obs_col] = "#"

        direction = "up"
        row, col = start_row, start_col
        steps = 0

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

            steps += 1

            # yeaaah it's ugly i know!
            if steps > rows * cols * 2:
                loops += 1
                break

        lab_map[obs_row][obs_col] = "."

print(loops)
