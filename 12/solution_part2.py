cache = {}


# The function is taken over from the following source:
# Source: https://github.com/hyper-neutrino/advent-of-code/blob/main/2023/day12p2.py
def count(cfg, nums):
    if cfg == "":
        return 1 if nums == () else 0

    if nums == ():
        return 0 if "#" in cfg else 1

    key = (cfg, nums)

    if key in cache:
        return cache[key]

    result = 0

    if cfg[0] in ".?":
        result += count(cfg[1:], nums)

    if cfg[0] in "#?":
        if nums[0] <= len(cfg) and "." not in cfg[:nums[0]] and (nums[0] == len(cfg) or cfg[nums[0]] != "#"):
            result += count(cfg[nums[0] + 1:], nums[1:])

    cache[key] = result
    return result


def main():
    with open('input') as f:
        lines = f.read().splitlines()
        lines = [line.split() for line in lines]

        records = [line[0] for line in lines]
        records_nums = [tuple(map(int, line[1].split(','))) for line in lines]

        records = ['?'.join([rec] * 5) for rec in records]
        records_nums = [rec_num * 5 for rec_num in records_nums]

        result_value = 0

        for rec, rec_nums in zip(records, records_nums):
            result_value = result_value + count(rec, rec_nums)

        print('The result is: ' + str(result_value))


if __name__ == "__main__":
    main()
