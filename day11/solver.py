from functools import wraps
from datetime import datetime
import numpy as np
import copy

total_time = []


def measure_time(func):
    @wraps(func)
    def _func(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        total_time.append((end - start).total_seconds())
        return result

    return _func


@measure_time
def parse(raw_data):
    grid = [list("b" + line + "b") for line in raw_data.strip().split("\n")]
    new_grid = [["b"] * len(grid[0])] + grid + [["b"] * len(grid[0])]

    return (grid, new_grid)


# PART 1
@measure_time
def solve1(data):
    copied = copy.deepcopy(data)
    return solve_general(copied, los=False, occupied_seats=4)


# PART 2
@measure_time
def solve2(data):
    copied = copy.deepcopy(data)
    return solve_general(copied, los=True, occupied_seats=5)


def solve_general(data, los=False, occupied_seats=4):

    grid, new_grid = data[0], data[1]
    width = len(grid[0])
    height = len(grid) + 2

    while grid != new_grid:
        # print("Iteration")
        grid = copy.deepcopy(new_grid)

        # print(grid)
        for y in range(1, height - 1):
            for x in range(1, width - 1):
                n_occupied_neighbours = sum(
                    "#" == line_of_sight(grid, x + dx, y + dy, dx, dy, los=los)
                    for dx in range(-1, 2)
                    for dy in range(-1, 2)
                    if (dx, dy) != (0, 0)
                )
                # print(grid[y][x], x, y, n_occupied_neighbours)
                if grid[y][x] == "L" and n_occupied_neighbours == 0:
                    new_grid[y][x] = "#"
                if grid[y][x] == "#" and n_occupied_neighbours >= occupied_seats:
                    new_grid[y][x] = "L"

    return sum(row.count("#") for row in grid)


def line_of_sight(grid, x, y, dx, dy, los=False):
    if not los:
        return grid[y][x]
    while grid[y][x] == ".":
        x, y = x + dx, y + dy
    return grid[y][x]


if __name__ == "__main__":
    import sys

    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("total time: {}s".format(sum(total_time)))
