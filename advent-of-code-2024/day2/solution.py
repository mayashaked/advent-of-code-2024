def main():

    num_safe = 0

    with open('input.txt', 'r') as file:
        for line in file:

            safe = True
            report = line.strip().split(' ')

            first_diff = int(report[1]) - int(report[0])
            first_diff_increasing = first_diff > 0
            biggest_diff = abs(first_diff)
            smallest_diff = abs(first_diff)

            for i in range(1, len(report)-1):
                diff = int(report[i+1]) - int(report[i])
                if diff == 0:
                    safe = False
                if abs(diff) > biggest_diff:
                    biggest_diff = abs(diff)
                else:
                    smallest_diff = abs(diff)

                diff_increasing = diff > 0
                if diff_increasing != first_diff_increasing:
                    safe = False
                if biggest_diff > 3:
                    safe = False
                if smallest_diff < 1:
                    safe = False

            if safe:
                num_safe += 1

    print(num_safe)
    return num_safe


if __name__ == "__main__":
    main()
