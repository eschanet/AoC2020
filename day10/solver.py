from functools import wraps
from datetime import datetime
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
    return [int(n) for n in raw_data.strip().split("\n")]


# PART 1
@measure_time
def solve1(data):
    ordered = sorted(data)
    prev_jolt = 0
    transitions = {1: 0, 2: 0, 3: 1}

    for jolt in ordered:
        transitions[jolt - prev_jolt] += 1
        prev_jolt = jolt

    return transitions[1] * transitions[3]


# PART 2
@measure_time
def solve2(data):
    ordered = [0] + sorted(data)
    options = defaultdict(int)
    options[0] = 1

    for jolt in ordered[1:]:
        options[jolt] = sum([options[jolt - i] for i in [1, 2, 3]])

    return options[ordered[-1]]


if __name__ == "__main__":
    import sys

    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("total time: {}s".format(sum(total_time)))
