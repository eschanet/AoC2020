from functools import wraps
from datetime import datetime
import copy

from collections import defaultdict

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
    return [int(n) for n in raw_data.strip().split(",")]


# PART 1
@measure_time
def solve1(data):
    return solve(data, 2020)


# PART 2
@measure_time
def solve2(data):
    return solve(data, 30000000)


def solve(data, limit):
    spoken = defaultdict(lambda: cnt)
    last_spoken = -1
    # prepopulate with input
    for cnt, n in enumerate(data):
        spoken[last_spoken] = cnt
        last_spoken = n
    # run up to limit
    for cnt in range(len(data), limit):
        # could write this in one line, but I find this more understandable
        cnt_last_spoken = spoken[last_spoken]
        spoken[last_spoken] = cnt
        last_spoken = cnt - cnt_last_spoken
    return last_spoken


if __name__ == "__main__":
    import sys

    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("total time: {}s".format(sum(total_time)))
