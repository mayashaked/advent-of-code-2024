def part1():

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

def part2():

    left_list = []
    right_list_val_dict = {}

    with open('input.txt', 'r') as file:
        for line in file:
            columns = line.strip().split('   ')
            if len(columns) == 2:
                left_list.append(int(columns[0]))

                right_list_val = int(columns[1])
                if right_list_val not in right_list_val_dict:
                    right_list_val_dict[right_list_val] = 1
                else:
                    right_list_val_dict[right_list_val] = right_list_val_dict[right_list_val] + 1
    similarity = 0
    for val in left_list:
        if val in right_list_val_dict:
            similarity += val * right_list_val_dict[val]

    print(similarity)
    return(similarity)



if __name__ == "__main__":
    part1()
    part2()


