def main():
    with open('input') as f:
        lines = f.readlines()

        result_value = 0

        for line in lines:
            history = list(map(int, line.split()))

            layers = [history]

            while not all([x == 0 for x in layers[-1]]):
                current_layer = []

                for i, j in zip(layers[-1], layers[-1][1:]):
                    diff = j - i
                    current_layer.append(diff)

                layers.append(current_layer)

            layers[-1].insert(0, 0)

            for i in range(len(layers) - 2, -1, -1):
                layers[i].insert(0, layers[i][0] - layers[i+1][0])

            result_value = result_value + layers[0][0]

        print('The result is: ' + str(result_value))


if __name__ == "__main__":
    main()
