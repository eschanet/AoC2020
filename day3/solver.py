from functools import wraps
from datetime import datetime
import numpy as np

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
    data = raw_data.strip().split("\n")
    return data


# PART 1
@measure_time
def solve1(data):
    return solve_for_steps(data, 3, 1)


# PART 2
@measure_time
def solve2(data):
    combs_to_check = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    results = [solve_for_steps(data, comb[0], comb[1]) for comb in combs_to_check]
    return np.product(results)


def solve_for_steps(data, x_step=3, y_step=1):
    x_dim = len(data[0])
    y_dim = len(data)
    x_pos = y_pos = n_trees = 0

    while y_pos < y_dim:
        if data[y_pos][x_pos % x_dim] == "#":
            n_trees += 1
        x_pos += x_step
        y_pos += y_step

    return n_trees


if __name__ == "__main__":
    import sys

    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("total time: {}s".format(sum(total_time)))
