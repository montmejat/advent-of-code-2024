ordering = []
updates = []
correct_updates = 0

with open("input.txt") as f:
    for line in f.read().splitlines():
        if "|" in line:
            ordering.append(tuple(int(i) for i in line.split("|")))
        if "," in line:
            updates.append(tuple(int(i) for i in line.split(",")))

for update in updates:
    correct = True
    # print("checking", update)

    for i, page in enumerate(update):
        # verify every pages before it
        # print(" checking page", page, f"({i})")

        for j in range(i):
            correct_before = False

            for before, after in ordering:
                if after == page and update[j] == before:
                    correct_before = True

            # print("  -> before:", update[j], correct_before)

            if not correct_before:
                correct = False

        # verify every pages after it
        for j in range(i + 1, len(update)):
            correct_after = False

            for before, after in ordering:
                if before == page and update[j] == after:
                    correct_after = True

            # print("  -> after:", update[j], correct_after)

            if not correct_after:
                correct = False

    if correct:
        correct_updates += update[len(update) // 2]

print(correct_updates)

