from functools import wraps
from datetime import datetime
from itertools import combinations
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
    data = [int(x) for x in raw_data.strip().split("\n")]
    return data


# PART 1
@measure_time
def solve1(data):
    return solve_n(data, 2)


# PART 2
@measure_time
def solve2(data):
    return solve_n(data, 3)


@measure_time
def solve_n(data, n):
    combs = list(combinations(data, n))
    for comb in combs:
        if np.sum(comb) == 2020:
            return np.product(comb)
    else:
        return False


if __name__ == "__main__":
    import sys

    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("total time: {}s".format(sum(total_time)))
