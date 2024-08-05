def is_valid_assignment(line, pattern):
    pattern_testing_num_idx = 0
    pattern_counter = pattern.copy()

    for symbol in line:
        if symbol == '#':
            if pattern_testing_num_idx < len(pattern_counter) and pattern_counter[pattern_testing_num_idx] > 0:
                pattern_counter[pattern_testing_num_idx] = pattern_counter[pattern_testing_num_idx] - 1
            else:
                return False
        elif symbol == '.':
            if pattern_counter[pattern_testing_num_idx] == 0:
                if pattern_testing_num_idx < len(pattern_counter) - 1:
                    pattern_testing_num_idx = pattern_testing_num_idx + 1
            elif pattern[pattern_testing_num_idx] != pattern_counter[pattern_testing_num_idx]:
                return False
        else:
            # symbol == '?'
            return False

    if pattern_testing_num_idx < len(pattern_counter) - 1 or pattern_counter[len(pattern_counter) - 1] != 0:
        return False

    return True


def get_line_arrangements_count(line, idx, pattern):
    combinations_num = 0
    line_len = len(line)

    # Iterate over other symbols.
    while idx < line_len and line[idx] != '?':
        idx = idx + 1

    if idx == line_len:
        return 0

    new_line = line.copy()
    new_line[idx] = '#'

    if is_valid_assignment(new_line, pattern):
        return 1
    else:
        combinations_num = combinations_num + get_line_arrangements_count(new_line, idx + 1, pattern)

    new_line = line.copy()
    new_line[idx] = '.'

    if is_valid_assignment(new_line, pattern):
        combinations_num = combinations_num + 1
    else:
        combinations_num = combinations_num + get_line_arrangements_count(new_line, idx + 1, pattern)

    return combinations_num


def main():
    with open('input') as f:
        lines = f.read().splitlines()
        lines = [line.split() for line in lines]

        records = [list(line[0]) for line in lines]
        records_nums = [list(map(int, line[1].split(','))) for line in lines]

        # Testing is_valid_assignment()
        # print(is_valid_assignment(list('.###.##....#'), [3, 2, 1]))

        # Testing get_line_arrangements_count()
        # print(get_line_arrangements_count(list('?###????????'), 0, [3, 2, 1]))

        result_value = 0

        for line, pattern in zip(records, records_nums):
            result_value = result_value + get_line_arrangements_count(line, 0, pattern)

        print('The result is: ' + str(result_value))


if __name__ == "__main__":
    main()
