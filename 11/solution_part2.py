# MUL_CONST = 9  # 10 -> 9
# MUL_CONST = 99  # 100 -> 99
MUL_CONST = 999999  # 1000000 -> 999999


def get_expansions_indexes(lines):
    empty_row = ['.'] * len(lines[0])
    empty_col = ['.'] * len(lines)

    new_rows_indexes = []
    new_cols_indexes = []

    # ROWS
    i = 0
    while i < len(lines):
        if lines[i] == empty_row:
            new_rows_indexes.append(i)

        i = i + 1

    # COLS
    i = 0
    while i < len(lines[0]):
        if [line[i] for line in lines] == empty_col:
            new_cols_indexes.append(i)

        i = i + 1

    return new_rows_indexes, new_cols_indexes


def get_nums_coords(lines):
    nums_coords = []

    for i, line in enumerate(lines):
        for j, x in enumerate(line):
            if x == '#':
                nums_coords.append((i, j))

    return nums_coords


def shortest_path(first_item_coords, second_item_coords, row_addition_count, col_addition_count):
    first_item_x = first_item_coords[1]
    first_item_y = first_item_coords[0]
    second_item_x = second_item_coords[1]
    second_item_y = second_item_coords[0]

    return (abs(first_item_x - second_item_x) + MUL_CONST * col_addition_count +
            abs(first_item_y - second_item_y) + MUL_CONST * row_addition_count)


def main():
    with open('input') as f:
        lines = f.read().splitlines()
        lines = [list(line) for line in lines]

        new_rows_indexes, new_cols_indexes = get_expansions_indexes(lines)
        nums_coords = get_nums_coords(lines)

        result_sum = 0

        for i, first_coords in enumerate(nums_coords):
            for second_coords in nums_coords[i+1:]:
                row_addition_count = 0

                for idx in new_rows_indexes:
                    range_min = min(first_coords[0], second_coords[0])
                    range_max = max(first_coords[0], second_coords[0])

                    if range_min < idx < range_max:
                        row_addition_count = row_addition_count + 1

                col_addition_count = 0
                for idx in new_cols_indexes:
                    range_min = min(first_coords[1], second_coords[1])
                    range_max = max(first_coords[1], second_coords[1])

                    if range_min < idx < range_max:
                        col_addition_count = col_addition_count + 1

                result_sum = result_sum + shortest_path(first_coords, second_coords, row_addition_count, col_addition_count)

        print('The result is: ' + str(result_sum))


if __name__ == "__main__":
    main()
