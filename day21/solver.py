from functools import wraps
from datetime import datetime
import regex as re
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
    regex = (
        r"(?:(?P<ingredients>\w+)(?: )?)+\(contains (?:(?P<allergenes>\w+)(?:, )?)+\)"
    )
    cnds = {}
    all_ingr = []

    for l in raw_data.strip().split("\n"):
        product = re.search(
            regex,
            l,
        ).capturesdict()
        all_ingr.extend(product["ingredients"])
        for allergene in product["allergenes"]:
            if allergene in cnds:
                cnds[allergene] &= set(product["ingredients"])
            else:
                cnds[allergene] = set(product["ingredients"])

    return (cnds, all_ingr)


# PART 1
@measure_time
def solve1(data):
    return solve(data, 1)


# PART 2
@measure_time
def solve2(data):
    return solve(data, 2)


def solve(data, mode=1):
    cands, all_ingr = copy.deepcopy(data[0]), copy.deepcopy(data[1])
    matched = {}
    while cands:
        for allergene, ingredient in list(cands.items()):
            if len(ingredient) == 1:
                matched[allergene] = ingredient.pop()
                del cands[allergene]
            else:
                cands[allergene] -= set(matched.values())
    if mode == 1:
        return len(
            [
                ingredient
                for ingredient in all_ingr
                if ingredient not in matched.values()
            ]
        )
    else:
        return ",".join([matched[key] for key in sorted(matched.keys())])


if __name__ == "__main__":
    import sys

    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("total time: {}s".format(sum(total_time)))
