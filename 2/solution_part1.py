import re


def main():
    red_conf = 12
    green_conf = 13
    blue_conf = 14

    with open('input') as f:
        lines = f.readlines()

        result_value = 0

        for line in lines:
            line_splitted = re.split(r'\W+', line)
            game_conf = line_splitted[2:len(line_splitted)]

            cubes_counts = game_conf[::2]
            cubes_colors = game_conf[1::2]

            valid_flag = True

            for count, color in zip(cubes_counts, cubes_colors):
                if color == 'red':
                    if int(count) > red_conf:
                        valid_flag = False
                elif color == 'green':
                    if int(count) > green_conf:
                        valid_flag = False
                elif color == 'blue':
                    if int(count) > blue_conf:
                        valid_flag = False
                else:
                    print('Uppssss, invalid input.')

            if valid_flag:
                result_value += int(line_splitted[1])

        print('The result is: ' + str(result_value))


if __name__ == "__main__":
    main()
