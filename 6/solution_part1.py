import math


def main():
    with open('input') as f:
        lines = f.readlines()

        result_value = 1

        times = list(map(int, lines[0].split()[1:]))
        distances = list(map(int, lines[1].split()[1:]))

        for time, distance in zip(times, distances):
            number_of_ways = 0
            peak_flag = False

            for i in range(math.ceil(distance / time), time):
                race_time = time - i
                speed = time-race_time

                if race_time * speed > distance:
                    peak_flag = True
                    number_of_ways = number_of_ways + 1
                elif peak_flag:
                    break

            result_value = result_value * number_of_ways

        print('The result is: ' + str(result_value))


if __name__ == "__main__":
    main()
