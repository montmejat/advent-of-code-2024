def check_safe(levels: list) -> bool:
    inc_or_dec = levels == sorted(levels) or levels == sorted(levels, reverse=True)
    if not inc_or_dec:
        return False

    safe = True
    for i in range(len(levels) - 1):
        diff = abs(levels[i] - levels[i + 1])
        if not 1 <= diff <= 3:
            safe = False
            break

    return safe


safe_counter = 0

with open("input.txt") as f:
    for idx, line in enumerate(f.read().splitlines()):
        levels = [int(x) for x in line.split(" ")]

        for i in range(len(levels)):
            sub_levels = levels[:i] + levels[i + 1 :]
            if check_safe(sub_levels):
                safe_counter += 1
                break


print(safe_counter)
