def main():

    with open('input') as f:
        lines = f.readlines()

        scratchcards_points = [0] * len(lines)

        for i, line in enumerate(lines):
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

            scratchcards_points[i] = matches

        scratchcards_counts = [1] * len(lines)

        scratchcards_total = 0

        for i in range(len(scratchcards_points)):
            while scratchcards_counts[i] > 0:
                for j in range(i+1, i+1+scratchcards_points[i]):
                    scratchcards_counts[j] = scratchcards_counts[j] + 1

                scratchcards_counts[i] = scratchcards_counts[i] - 1
                scratchcards_total = scratchcards_total + 1

        print('The result is: ' + str(scratchcards_total))


if __name__ == "__main__":
    main()
