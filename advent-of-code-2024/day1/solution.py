def main():
    left_list = []
    right_list = []

    with open('input.txt', 'r') as file:
        for line in file:
            columns = line.strip().split('   ')
            if len(columns) == 2:
                left_list.append(int(columns[0]))
                right_list.append(int(columns[1]))

    if len(left_list) == 0 or len(right_list) == 0:
        return []

    left_list.sort()
    right_list.sort()

    distance = 0
    for i in range(len(left_list)):
        distance += abs(left_list[i] - right_list[i])
    print(distance)
    return(distance)



if __name__ == "__main__":
    main()


