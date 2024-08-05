def main():

    with open('input') as f:
        lines = f.readlines()

        result_value = 0

        for line in lines:
            colon_idx = line.find(':')
            line = line[colon_idx + 1:]

            line_splitted = line.split('|')

            winning_numbers = line_splitted[0]
            own_numbers = line_splitted[1]

            winning_numbers = winning_numbers.split()
            own_numbers = own_numbers.split()

            winning_numbers.sort()
            own_numbers.sort()

            winning_numbers_iterator, own_numbers_iterator = (0, 0)

            matches = 0

            while winning_numbers_iterator < len(winning_numbers) and own_numbers_iterator < len(own_numbers):
                if winning_numbers[winning_numbers_iterator] == own_numbers[own_numbers_iterator]:
                    matches = matches + 1
                    winning_numbers_iterator = winning_numbers_iterator + 1
                    own_numbers_iterator = own_numbers_iterator + 1
                elif winning_numbers[winning_numbers_iterator] < own_numbers[own_numbers_iterator]:
                    winning_numbers_iterator = winning_numbers_iterator + 1
                else:
                    # winning_numbers[winning_numbers_iterator] > own_numbers[own_numbers_iterator]
                    own_numbers_iterator = own_numbers_iterator + 1

            if matches > 0:
                result_value = result_value + 2**(matches - 1)

        print('The result is: ' + str(result_value))


if __name__ == "__main__":
    main()
