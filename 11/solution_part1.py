def expand(lines):
    empty_row = ['.'] * len(lines[0])
    empty_col = ['.'] * len(lines)

    new_rows_indexes = []
    new_cols_indexes = []

    # ROWS
    i = 0
    while i < len(lines):
        if lines[i] == empty_row:
            new_rows_indexes.append(i + len(new_rows_indexes))

        i = i + 1

    # COLS
    i = 0
    while i < len(lines[0]):
        if [line[i] for line in lines] == empty_col:
            new_cols_indexes.append(i + len(new_cols_indexes))

        i = i + 1

    # Insert new rows and cols.
    for idx in new_rows_indexes:
        lines.insert(idx, ['.'] * len(lines[0]))

    for i in range(len(lines)):
        for idx in new_cols_indexes:
            lines[i].insert(idx, '.')

    return lines


def get_nums_coords(lines):
    nums_coords = []

    for i, line in enumerate(lines):
        for j, x in enumerate(line):
            if x == '#':
                nums_coords.append((i, j))

    return nums_coords


def shortest_path(first_item_coords, second_item_coords):
    first_item_x = first_item_coords[1]
    first_item_y = first_item_coords[0]
    second_item_x = second_item_coords[1]
    second_item_y = second_item_coords[0]

    return abs(first_item_x - second_item_x) + abs(first_item_y - second_item_y)


def main():
    with open('input') as f:
        lines = f.read().splitlines()
        lines = [list(line) for line in lines]

        grid = expand(lines)
        nums_coords = get_nums_coords(grid)

        result_sum = 0

        for i, first_coords in enumerate(nums_coords):
            for second_coords in nums_coords[i+1:]:
                result_sum = result_sum + shortest_path(first_coords, second_coords)

        print('The result is: ' + str(result_sum))


if __name__ == "__main__":
    main()
