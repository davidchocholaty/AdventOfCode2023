import math


def main():
    with open('input') as f:
        lines = f.readlines()

        time = int(''.join(lines[0].split()[1:]))
        distance = int(''.join(lines[1].split()[1:]))

        i = math.ceil(distance / time)

        low = 0
        high = time

        while low == 0:
            race_time = time - i
            speed = time - race_time

            if race_time * speed > distance:
                low = i

            i = i + 1

        i = high - i + 1

        while time == high:
            race_time = time - i
            speed = time - race_time

            if race_time * speed > distance:
                high = i

            i = i - 1

        print('The result is: ' + str(high - low + 1))


if __name__ == "__main__":
    main()
