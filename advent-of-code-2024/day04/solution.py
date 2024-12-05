def part1():

    crossword = []
    with open('input.txt', 'r') as file:
        for line in file:
            crossword.append(line.strip())

    X_locs = find_X_locs(crossword)
    return num_has_MAS_after_X(crossword, X_locs)

def find_X_locs(crossword):

    X_locs = []

    for rownum in range(len(crossword)):
        for colnum in range(len(crossword[0])):
            letter = crossword[rownum][colnum]
            if letter == 'X':
                X_locs.append([rownum, colnum])
    return(X_locs)

def num_has_MAS_after_X(crossword, X_locs):

    num_has_MAS_after_X = 0

    for X_loc in X_locs:
        has_right_MAS = _has_MAS_after_X_directional(
            crossword=crossword,
            X_loc=X_loc,
            add_to_rownum = [0, 0, 0],
            add_to_colnum= [1, 2, 3]
        )
        num_has_MAS_after_X += has_right_MAS

        has_left_MAS = _has_MAS_after_X_directional(
            crossword=crossword,
            X_loc=X_loc,
            add_to_rownum = [0, 0, 0],
            add_to_colnum= [-1, -2, -3]
        )
        num_has_MAS_after_X += has_left_MAS

        has_upper_MAS = _has_MAS_after_X_directional(
            crossword=crossword,
            X_loc=X_loc,
            add_to_rownum = [-1, -2, -3],
            add_to_colnum= [0, 0, 0]
        )
        num_has_MAS_after_X += has_upper_MAS

        has_lower_MAS = _has_MAS_after_X_directional(
            crossword=crossword,
            X_loc=X_loc,
            add_to_rownum = [1, 2, 3],
            add_to_colnum= [0, 0, 0]
        )
        num_has_MAS_after_X += has_lower_MAS

        has_right_upper_MAS = _has_MAS_after_X_directional(
            crossword=crossword,
            X_loc=X_loc,
            add_to_rownum = [-1, -2, -3],
            add_to_colnum= [1, 2, 3]
        )
        num_has_MAS_after_X += has_right_upper_MAS

        has_right_lower_MAS = _has_MAS_after_X_directional(
            crossword=crossword,
            X_loc=X_loc,
            add_to_rownum = [1, 2, 3],
            add_to_colnum= [1, 2, 3]
        )
        num_has_MAS_after_X += has_right_lower_MAS

        has_left_lower_MAS = _has_MAS_after_X_directional(
            crossword=crossword,
            X_loc=X_loc,
            add_to_rownum = [1, 2, 3],
            add_to_colnum= [-1, -2, -3]
        )
        num_has_MAS_after_X += has_left_lower_MAS

        has_left_upper_MAS = _has_MAS_after_X_directional(
            crossword=crossword,
            X_loc=X_loc,
            add_to_rownum = [-1, -2, -3],
            add_to_colnum= [-1, -2, -3]
        )
        num_has_MAS_after_X += has_left_upper_MAS

    print(num_has_MAS_after_X)
    return(num_has_MAS_after_X)

def _has_MAS_after_X_directional(crossword, X_loc, add_to_rownum, add_to_colnum):

    [X_rownum, X_colnum] = X_loc

    row_one_next, col_one_next = X_rownum + add_to_rownum[0], X_colnum + add_to_colnum[0]
    row_two_next, col_two_next = X_rownum + add_to_rownum[1], X_colnum + add_to_colnum[1]
    row_three_next, col_three_next = X_rownum + add_to_rownum[2], X_colnum + add_to_colnum[2]

    if (row_one_next >= 0) and (col_one_next >= 0) and (
        row_two_next >= 0) and (col_two_next >= 0) and (
        row_three_next >= 0) and (col_three_next >= 0) and (
        row_one_next < len(crossword)) and (col_one_next < len(crossword[0])) and (
        row_two_next < len(crossword)) and (col_two_next < len(crossword[0])) and (
        row_three_next < len(crossword)) and (col_three_next < len(crossword[0])
    ):

        (one_next, two_next, three_next) = (
            crossword[row_one_next][col_one_next],
            crossword[row_two_next][col_two_next],
            crossword[row_three_next][col_three_next]
        )
        if one_next == 'M' and two_next == 'A' and three_next == 'S':
            return 1
        else:
            return 0
    else:
        return 0

def part2():

    crossword = []
    with open('input.txt', 'r') as file:
        for line in file:
            crossword.append(line.strip())

    A_locs = find_A_locs(crossword)
    return num_has_MS_cross(crossword, A_locs)

def find_A_locs(crossword):

    A_locs = []

    for rownum in range(len(crossword)):
        for colnum in range(len(crossword[0])):
            letter = crossword[rownum][colnum]
            if letter == 'A':
                A_locs.append([rownum, colnum])
    return(A_locs)

def num_has_MS_cross(crossword, A_locs):

    num_cross = 0
    for A_loc in A_locs:

        [A_rownum, A_colnum] = A_loc

        if A_rownum > 0 and A_colnum > 0 and A_rownum < len(crossword[0])-1 and A_colnum < len(crossword[0])-1:

            top_left = crossword[A_rownum-1][A_colnum-1]
            top_right = crossword[A_rownum-1][A_colnum+1]
            bottom_left = crossword[A_rownum+1][A_colnum-1]
            bottom_right = crossword[A_rownum+1][A_colnum+1]

            if (
                    top_left == 'M' and top_right == 'S' and bottom_left == 'M' and bottom_right == 'S'
            ) or (
                    top_left == 'M' and top_right == 'M' and bottom_left == 'S' and bottom_right == 'S'
            ) or (
                    top_left == 'S' and top_right == 'M' and bottom_left == 'S' and bottom_right == 'M'
            ) or (
                    top_left == 'S' and top_right == 'S' and bottom_left == 'M' and bottom_right == 'M'
            ):
                num_cross += 1

    print(num_cross)
    return num_cross


if __name__ == "__main__":
    part1()
    part2()
