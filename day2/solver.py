from functools import wraps
from datetime import datetime

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
    data = [
        (
            int(x.split(" ")[0].split("-")[0]),
            int(x.split(" ")[0].split("-")[1]),
            x.split(" ")[1].replace(":", ""),
            x.split(" ")[2],
        )
        for x in raw_data.strip().split("\n")
    ]
    return data


# PART 1
@measure_time
def solve1(data):
    valid = []  # for potential debugging, using list instead of simple counter
    for entry in data:
        pwd = entry[3]
        letter = entry[2]
        n = pwd.count(letter)
        if n >= entry[0] and n <= entry[1]:
            valid.append(entry)
    return len(valid)


# PART 2
@measure_time
def solve2(data):
    valid = []  # for potential debugging, using list instead of simple counter
    for entry in data:
        pwd = entry[3]
        letter = entry[2]
        if (letter == pwd[entry[0] - 1]) and (letter == pwd[entry[1] - 1]):
            continue
        if (letter == pwd[entry[0] - 1]) or (letter == pwd[entry[1] - 1]):
            valid.append(entry)
    return len(valid)


if __name__ == "__main__":
    import sys

    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("total time: {}s".format(sum(total_time)))
