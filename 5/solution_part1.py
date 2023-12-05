import re


def main():
    with open('input') as f:
        seeds_and_maps = f.read().strip().split('\n\n')

        seeds = seeds_and_maps[0]
        maps = seeds_and_maps[1:]

        mapping_source = re.findall(r'\d+', seeds)

        if not mapping_source:
            print('Uppssss, error.')
            return

        mapping_source = list(map(int, mapping_source))
        mapping_source_modification = [False] * len(mapping_source)

        for mapping in maps:
            mapping_vals = re.findall(r'\d+', mapping)

            if not mapping_vals:
                print('Uppssss, error.')
                return

            for i in range(0, len(mapping_vals), 3):
                source_range_start = int(mapping_vals[i+1])
                source_range_end = source_range_start + int(mapping_vals[i+2])

                for j in range(len(mapping_source)):
                    if not mapping_source_modification[j]:
                        if source_range_start <= mapping_source[j] <= source_range_end:
                            diff = mapping_source[j] - source_range_start
                            mapping_source[j] = int(mapping_vals[i]) + diff
                            mapping_source_modification[j] = True

            mapping_source_modification = [False] * len(mapping_source)

        result_value = min(mapping_source)

        print('The result is: ' + str(result_value))


if __name__ == "__main__":
    main()
