
def part1():

    rules = load_data(filename='page_orders.txt', delimiter="|")
    updates = load_data(filename='updates.txt', delimiter=",")

    faulty_updates = []
    for rule_pair in rules: # get rules
        to_print_before, to_print_after = rule_pair
        for i, update in enumerate(updates): # go through each update
            if to_print_before in update and to_print_after in update: # check whether rule pair combo is in update
                if update.index(to_print_before) > update.index(to_print_after): # check for incorrect order
                    if i not in faulty_updates:
                        faulty_updates.append(i) # save index of faulty updates

    correct_updates_middle_sum = 0
    for i, update in enumerate(updates):
        if i not in faulty_updates: # we only want the correctly-ordered updates
            correct_updates_middle_sum += update[len(update)//2] # get middle value in update list

    print(correct_updates_middle_sum)
    return(correct_updates_middle_sum)


def load_data(filename, delimiter):
    data = []
    with open(filename, 'r') as file:
        for row in file:
            str_list = row.strip("\n").split(delimiter)
            data.append([int(x) for x in str_list])
    return(data)

if __name__ == "__main__":
    part1()
