import re


def main():
    values_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    with (open('input') as f):
        lines = f.readlines()

        result_value = 0

        for line in lines:
            match_str = r'(?=(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))'
            matches = re.finditer(match_str, line)

            match = [match.group(1) for match in matches]

            if match:
                forward_value = match[0] if len(match[0]) == 1 else values_dict[match[0]]
                backward_value = match[-1] if len(match[-1]) == 1 else values_dict[match[-1]]

                result_value = result_value + int(forward_value + backward_value)

            else:
                print('Uppssss, error.')

        print('The result is: ' + str(result_value))


if __name__ == "__main__":
    main()
