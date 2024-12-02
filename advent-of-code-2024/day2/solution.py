def part1():

    num_safe = 0

    with open('input.txt', 'r') as file:
        for line in file:

            report = line.strip().split(' ')

            if is_safe(report):
                num_safe += 1

    print(num_safe)
    return num_safe

def part2():

    num_safe = 0

    with open('input.txt', 'r') as file:
        for line in file:

            report = line.strip().split(' ')

            if is_safe(report):
                num_safe += 1
            else:
                num_is_safe_with_one_removed = 0
                for idx in range(len(report)):
                    report_with_one_removed = [x for i, x in enumerate(report) if i != idx]
                    if is_safe(report_with_one_removed):
                        num_is_safe_with_one_removed += 1
                if num_is_safe_with_one_removed > 0:
                    num_safe += 1

    print(num_safe)
    return num_safe

def is_safe(report):

    first_diff = int(report[1]) - int(report[0])
    first_diff_increasing = first_diff > 0
    biggest_diff = abs(first_diff)
    smallest_diff = abs(first_diff)

    safe = True
    for i in range(1, len(report) - 1):
        diff = int(report[i + 1]) - int(report[i])
        if diff == 0:
            safe = False
        elif abs(diff) > biggest_diff:
            biggest_diff = abs(diff)
        else:
            smallest_diff = abs(diff)

        diff_increasing = diff > 0
        if (diff_increasing != first_diff_increasing) or (biggest_diff > 3) or (smallest_diff < 1):
            safe = False

    return(safe)


if __name__ == "__main__":
    part1()
    part2()
