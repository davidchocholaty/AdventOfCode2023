def test_gear(symbol, number, line, col, gears):
    if symbol == '*':
        gears[line][col].append(int(number))


def main():
    with (open('input') as f):
        lines = f.read().strip().split('\n')

        result_value = 0

        number_of_lines = len(lines)
        lines_len = len(lines[0])

        gears = [[[] for _ in range(lines_len)] for _ in range(number_of_lines)]

        prev_line = None

        # Iterate through lines.
        for i, line in enumerate(lines):
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                next_line = next_line[:len(line) - 1]
            else:
                next_line = None

            j = 0

            # Iterate through single line.
            while j < lines_len:
                symbols = line[j]

                # Test if symbol is a digit.
                if symbols.isdigit():
                    number_start_idx = j

                    while j + 1 < lines_len and line[j + 1].isdigit():
                        j = j + 1
                        symbols = symbols + line[j]

                    # In symbols is whole number.

                    prev_symbol_idx = max(0, number_start_idx - 1)
                    next_symbol_idx = min(lines_len - 1, j + 1)

                    # The current line.
                    test_gear(line[prev_symbol_idx], symbols, i, prev_symbol_idx, gears)
                    test_gear(line[next_symbol_idx], symbols, i, next_symbol_idx, gears)

                    # The previous line.
                    if prev_line:
                        for k in range(max(0, number_start_idx - 1), min(lines_len - 1, j + 2)):
                            test_gear(prev_line[k], symbols, i-1, k, gears)

                    # The next line.
                    if next_line:
                        for k in range(max(0, number_start_idx - 1), min(lines_len - 1, j + 2)):
                            test_gear(next_line[k], symbols, i+1, k, gears)

                j = j + 1

            prev_line = line

        for i in range(number_of_lines):
            for j in range(lines_len):
                gear_numbers = gears[i][j]

                if lines[i][j] == '*' and len(gear_numbers) == 2:
                    result_value = result_value + gear_numbers[0] * gear_numbers[1]

        print('The result is: ' + str(result_value))


if __name__ == "__main__":
    main()
