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
    data = [d.replace("\n", " ").split(" ") for d in raw_data.strip().split("\n\n")]
    return data


# PART 1
@measure_time
def solve1(data):
    answers = [unique_letters(group) for group in data]
    return sum(answers)


# PART 2
@measure_time
def solve2(data):
    answers = [common_answers(group) for group in data]
    return sum(answers)


def unique_letters(
    answers, letters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
):
    counter = 0
    for i in letters:
        for answer in answers:
            if i in answer:
                counter += 1
                break
    return counter


def common_answers(
    answers, letters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
):
    counter = 0
    for i in letters:
        for answer in answers:
            if not i in answer:
                break
        else:
            counter += 1
    return counter


if __name__ == "__main__":
    import sys

    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("total time: {}s".format(sum(total_time)))
