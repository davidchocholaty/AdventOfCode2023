import re


def main():
    with open('input') as f:
        lines = f.readlines()

        result_value = 0

        for line in lines:
            match_forward = re.search(r'\d', line)
            match_backward = re.search(r'\d', line[::-1])

            if match_forward and match_backward:
                result_value = result_value + int(match_forward.group() + match_backward.group())
            else:
                print('Uppssss, error.')

        print('The result is: ' + str(result_value))


if __name__ == "__main__":
    main()
