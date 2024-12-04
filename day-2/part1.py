safe_counter = 0

with open("input.txt") as f:
    for line in f.read().splitlines():
        levels = [int(x) for x in line.split(" ")]

        if len(levels) != len(set(levels)):
            continue

        increasing = levels[0] < levels[1]
        safe = True

        for i in range(len(levels) - 1):
            diff = levels[i + 1] - levels[i]

            if increasing and (diff < 0 or diff > 3):
                safe = False
                break
            elif not increasing and (diff > 0 or diff < -3):
                safe = False
                break

        if safe:
            safe_counter += 1

print(safe_counter)
