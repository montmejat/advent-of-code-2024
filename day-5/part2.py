ordering = []
updates = []
score = 0


def switch(left_page: int, right_page: int):
    for before, after in ordering:
        if before == left_page and after == right_page:
            return False
        if before == right_page and after == left_page:
            return True


with open("input.txt") as f:
    for line in f.read().splitlines():
        if "|" in line:
            ordering.append(tuple(int(i) for i in line.split("|")))
        if "," in line:
            updates.append([int(i) for i in line.split(",")])

for update in updates:
    correct = True

    for i, page in enumerate(update):
        # verify every pages before it
        for j in range(i):
            correct_before = False

            for before, after in ordering:
                if after == page and update[j] == before:
                    correct_before = True

            if not correct_before:
                correct = False

        # verify every pages after it
        for j in range(i + 1, len(update)):
            correct_after = False

            for before, after in ordering:
                if before == page and update[j] == after:
                    correct_after = True

            if not correct_after:
                correct = False

    if not correct:
        for i in range(len(update) - 1, 0, -1):
            for j in range(i):
                if switch(update[j], update[j + 1]):
                    temp = update[j]
                    update[j] = update[j + 1]
                    update[j + 1] = temp

        score += update[len(update) // 2]

print(score)

