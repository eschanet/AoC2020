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
    return [int(n) for n in raw_data.strip().split("\n")]


# PART 1
@measure_time
def solve1(data, preamble_length=25):
    for n in range(preamble_length, len(data) - preamble_length):
        preamble = data[n - preamble_length : n]
        combs = np.array(list(combinations(preamble, 2)))
        matches = combs[np.sum(combs, axis=1) == data[n]]
        if matches.size == 0 or np.all(matches[:, 0] == matches[:, 1], axis=0):
            return data[n]


# PART 2
@measure_time
def solve2(data, result_solve1):

    # partial sums, should be O(n)
    cusums = [0]
    a, b = 0, 0
    while True:
        partial_sum = cusums[b] - cusums[a]
        if partial_sum > result_solve1:
            a += 1
        elif partial_sum < result_solve1:
            cusums.append(cusums[-1] + data[b])
            b += 1
        else:
            break

    seq = data[a:b]
    return min(seq) + max(seq)

    # keep my initial solution for reference
    # idxs = list(range(len(data)))
    # for start, end in combinations(idxs, 2):
    #     if sum(data[start : end + 1]) == result_solve1:
    #         return min(data[start : end + 1]) + max(data[start : end + 1])


if __name__ == "__main__":
    import sys

    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data, solve1(data))))

    print("total time: {}s".format(sum(total_time)))
