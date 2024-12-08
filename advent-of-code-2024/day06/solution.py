def part1():

    lab_map = []
    obstruction_positions = []
    row_index = 0
    with open('input.txt', 'r') as file:
        for line in file:
            lab_map.append(line.strip("\n"))
            for column_index, symbol in enumerate(line):
                if symbol == "#":
                    obstruction_positions.append([row_index, column_index])
                elif symbol == "^":
                    guard_position = [row_index, column_index]

            row_index += 1

    num_rows = len(lab_map)
    num_cols = len(lab_map[0])
    guard_symbol = "^"
    direction_key = {
        "^" : {"row_move": -1, "col_move": 0, "next_symbol": ">"},
        ">" : {"row_move" :0, "col_move": 1, "next_symbol": "v"},
        "v" : {"row_move": 1, "col_move": 0, "next_symbol": "<"},
        "<" : {"row_move": 0, "col_move": -1, "next_symbol": "^"}
    }

    distinct_positions = [guard_position]
    while guard_position[0] < num_rows and guard_position[1] < num_cols:
        next_position_row = guard_position[0] + direction_key[guard_symbol]["row_move"]
        next_position_col = guard_position[1] + direction_key[guard_symbol]["col_move"]

        if next_position_row == num_rows or next_position_col == num_cols:
            print(len(distinct_positions))
            return (len(distinct_positions))
        next_symbol = lab_map[next_position_row][next_position_col]

        if next_symbol == "#":
            guard_symbol = direction_key[guard_symbol]["next_symbol"]
        else:
            guard_position = [next_position_row, next_position_col]
            if guard_position not in distinct_positions:
                distinct_positions.append(guard_position)


if __name__ == "__main__":
    part1()
