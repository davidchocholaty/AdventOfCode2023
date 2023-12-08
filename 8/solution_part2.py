import math
import re


def is_valid_ending_configuration(configurations):
    for configuration in configurations:
        if not configuration.endswith('Z'):
            return False

    return True


def main():
    with open('input') as f:
        lines = f.readlines()

        lr_insts = lines[0].split()[0]
        nodes = lines[2:]

        nodes_mapping = {}
        configurations = []

        for node in nodes:
            splitted_node = node.split(' = ')

            matches = re.findall(r'[A-Z0-9]+', splitted_node[1])
            if not matches:
                print('Uppssss, invalid input.')
                return

            nodes_mapping[splitted_node[0]] = matches

            if splitted_node[0].endswith('A'):
                configurations.append(splitted_node[0])

        configurations_steps = [0] * len(configurations)

        for i, configuration in enumerate(configurations):
            cur_node = configuration
            counter = 0

            while not cur_node.endswith('Z'):
                if lr_insts[counter % len(lr_insts)] == 'L':
                    # step == 'L'
                    cur_node = nodes_mapping[cur_node][0]
                else:
                    # step == 'R'
                    cur_node = nodes_mapping[cur_node][1]

                counter = counter + 1

            configurations_steps[i] = counter

        result_value = math.lcm(*configurations_steps)

        print('The result is: ' + str(result_value))


if __name__ == "__main__":
    main()
