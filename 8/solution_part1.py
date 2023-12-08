import re


def main():
    with open('input') as f:
        lines = f.readlines()

        lr_insts = lines[0].split()[0]
        nodes = lines[2:]

        cur_node = 'AAA'

        nodes_mapping = {}

        for node in nodes:
            splitted_node = node.split(' = ')

            matches = re.findall(r'[A-Z]+', splitted_node[1])
            if not matches:
                print('Uppssss, invalid input.')
                return

            nodes_mapping[splitted_node[0]] = matches

        counter = 0

        while cur_node != 'ZZZ':
            if lr_insts[counter % len(lr_insts)] == 'L':
                # step == 'L'
                cur_node = nodes_mapping[cur_node][0]
            else:
                # step == 'R'
                cur_node = nodes_mapping[cur_node][1]

            counter = counter + 1

        print('The result is: ' + str(counter))


if __name__ == "__main__":
    main()
