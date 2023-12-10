# The solution is inspired from the following source:
# https://github.com/womogenes/AoC-2023-Solutions/blob/main/day_10/day_10_p1.py

from collections import deque


def get_index(symbol, lines):
    for i, line in enumerate(lines):
        if symbol in line:
            return i, line.index(symbol)
    return -1, -1


def get_neighbours(position, lines):
    neighbours = []

    for i, j in list(get_direct_neighbours((position[0], position[1]), lines)):
        y_new = position[0] + i
        x_new = position[1] + j

        if 0 <= y_new <= len(lines) and 0 <= x_new <= len(lines[0]):
            neighbours.append((y_new, x_new))

    return neighbours


def get_direct_neighbours(position, lines):
    if lines[position[0]][position[1]] == 'S':
        neighbours = []

        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            y_new = position[0] + i
            x_new = position[1] + j

            if 0 <= y_new <= len(lines) and 0 <= x_new <= len(lines[0]):
                if position in list(get_neighbours((y_new, x_new), lines)):
                    neighbours.append((i, j))
        return neighbours

    return {
        '|': [(1, 0), (-1, 0)],
        '-': [(0, 1), (0, -1)],
        'L': [(-1, 0), (0, 1)],
        'J': [(-1, 0), (0, -1)],
        '7': [(1, 0), (0, -1)],
        'F': [(1, 0), (0, 1)],
        '.': [],
    }[lines[position[0]][position[1]]]


# The function is taken from the following source:
# https://pieriantraining.com/bfs-breadth-first-search-implementation-in-python/
def get_bfs_distances(lines, start):
    distances = {}

    visited = set()
    queue = deque([start])
    while queue:
        position, distance = queue.popleft()
        if position not in visited:
            visited.add(position)
            distances[position] = distance

            for neighbour in list(get_neighbours(position, lines)):
                if neighbour not in visited:
                    queue.append((neighbour, distance + 1))

    return distances


def main():
    with open('input') as f:
        lines = f.readlines()

        for i in range(len(lines)):
            lines[i] = lines[i].split()[0]

        lines = [list(line) for line in lines]
        s_coords = get_index('S', lines)

        distances = get_bfs_distances(lines, (s_coords, 0))

        print('The result is: ' + str(max(distances.values())))


if __name__ == "__main__":
    main()
