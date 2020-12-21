from functools import wraps
from datetime import datetime
from itertools import product

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
    part1 = {
        (x, y, 0)  # 3 dimensions
        for x, row in enumerate(raw_data.split("\n"))
        for y, cell in enumerate(row)
        if cell == "#"
    }
    part2 = {
        (x, y, 0, 0)  # 4 dimensions
        for x, row in enumerate(raw_data.split("\n"))
        for y, cell in enumerate(row)
        if cell == "#"
    }

    return (part1, part2)


# PART 1
@measure_time
def solve1(data):
    return solve(data, 1)


# PART 2
@measure_time
def solve2(data):
    return solve(data, 2)


def solve(data, part=1):
    d = data[part - 1]

    def live_or_die(c):
        n = len(d & set(product(*[range(a - 1, a + 2) for a in c])))
        return n == 4 and c in d or n == 3

    for cycle in range(6):
        d = set(
            filter(live_or_die, product(range(-cycle - 1, cycle + 8), repeat=2 + part))
        )

    return len(d)


if __name__ == "__main__":
    import sys

    data = parse(open("input.txt").read().strip())

    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("total time: {}s".format(sum(total_time)))
