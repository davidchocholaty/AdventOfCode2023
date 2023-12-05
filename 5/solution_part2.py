# The solution is inspired from the following source:
# https://github.com/hyper-neutrino/advent-of-code/blob/main/2023/day05p2.py

def main():
    with open('input') as f:
        seeds_and_maps = f.read().strip().split('\n\n')
        seeds_input = list(map(int, seeds_and_maps[0].split(":")[1].split()))
        maps_input = seeds_and_maps[1:]

        seeds = []

        for i in range(0, len(seeds_input), 2):
            seeds.append((seeds_input[i], seeds_input[i] + seeds_input[i + 1]))

        for mapping in maps_input:
            ranges = []

            for line in mapping.splitlines()[1:]:
                ranges.append(list(map(int, line.split())))

            new_ranges = []

            while len(seeds) > 0:
                seed_range_start, seed_range_end = seeds.pop()

                for dest, source, range_len in ranges:
                    range_start = max(seed_range_start, source)
                    range_end = min(seed_range_end, source + range_len)

                    if range_start < range_end:
                        new_ranges.append((range_start - source + dest, range_end - source + dest))

                        if range_start > seed_range_start:
                            seeds.append((seed_range_start, range_start))
                        if seed_range_end > range_end:
                            seeds.append((range_end, seed_range_end))
                        break
                else:
                    new_ranges.append((seed_range_start, seed_range_end))

            seeds = new_ranges

        print('The result is: ' + str(min(seeds)[0]))


if __name__ == "__main__":
    main()
