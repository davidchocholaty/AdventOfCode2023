def is_symbol(symbol):
    return symbol != '.' and not symbol.isdigit()


def main():
    with open('input') as f:
        lines = f.read().strip().split('\n')

        result_value = 0

        lines_len = len(lines[0])

        prev_line = None

        # Iterate through lines.
        for i, line in enumerate(lines):
            if i + 1 < len(lines):
                next_line = lines[i+1]
                next_line = next_line[:len(line)-1]
            else:
                next_line = None

            j = 0

            # Iterate through single line.
            while j < lines_len:
                symbols = line[j]

                # Test if symbol is a digit.
                if symbols.isdigit():
                    is_part_number = False
                    number_start_idx = j

                    while j+1 < lines_len and line[j+1].isdigit():
                        j = j + 1
                        symbols = symbols + line[j]

                    # In symbols is whole number.

                    # The current line.
                    if is_symbol(line[max(0, number_start_idx-1)]) or is_symbol(line[min(lines_len-1, j+1)]):
                        is_part_number = True
                    else:
                        # The previous line.
                        if prev_line:
                            for k in range(max(0, number_start_idx-1), min(lines_len-1, j+2)):
                                if is_symbol(prev_line[k]):
                                    is_part_number = True
                                    break

                        # The next line.
                        if next_line and not is_part_number:
                            for k in range(max(0, number_start_idx-1), min(lines_len-1, j+2)):
                                if is_symbol(next_line[k]):
                                    is_part_number = True
                                    break

                    if is_part_number:
                        result_value = result_value + int(symbols)

                j = j + 1

            prev_line = line

        print('The result is: ' + str(result_value))


if __name__ == "__main__":
    main()
