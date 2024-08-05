import re


def main():
    with open('input') as f:
        lines = f.readlines()

        result_value = 0

        for line in lines:
            line_splitted = re.split(r'\W+', line)
            game_conf = line_splitted[2:len(line_splitted)]

            cubes_counts = game_conf[::2]
            cubes_colors = game_conf[1::2]

            red_count = 0
            green_count = 0
            blue_count = 0

            for count, color in zip(cubes_counts, cubes_colors):
                if color == 'red':
                    red_count = max(red_count, int(count))
                elif color == 'green':
                    green_count = max(green_count, int(count))
                elif color == 'blue':
                    blue_count = max(blue_count, int(count))
                else:
                    print('Uppssss, invalid input.')

            result_value += red_count * green_count * blue_count

        print('The result is: ' + str(result_value))


if __name__ == "__main__":
    main()
