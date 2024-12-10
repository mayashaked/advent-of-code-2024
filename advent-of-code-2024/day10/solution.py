def main():
    data = [list(map(int, x)) for x in open('input.txt').read().split('\n')]
    result = []

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 0:
                traverse((i, j), (i, j))

    print(f"Part 1: {len(set(result))}")
    print(f"Part 2: {len(result)}")

def traverse(loc, first_loc):
    if get_value_at_loc(loc) == 9:
        result.append((loc, first_loc))

    next_positions = [(loc[0] + 1, loc[1]), (loc[0] - 1, loc[1]), (loc[0], loc[1] + 1), (loc[0], loc[1] - 1)]

    for next_pos in next_positions:
        if bounds_ok(next_pos) and get_value_at_loc(next_pos) == get_value_at_loc(loc) + 1:
            traverse(next_pos, first_loc)

def get_value_at_loc(p):
    return data[p[0]][p[1]]

def bounds_ok(p):
    if (p[0] > len(data) - 1 or p[0] < 0 or p[1] > len(data) - 1 or p[1] < 0):
        return False
    return True


if __name__ == "__main__":
    main()
