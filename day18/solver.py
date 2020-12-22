from functools import wraps
from datetime import datetime
from more_itertools import chunked
from collections import deque
from math import prod

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
    return raw_data.strip().split("\n")


# PART 1
@measure_time
def solve1(data):
    return sum(evaluate(line, eval1) for line in data)


# PART 2
@measure_time
def solve2(data):
    return sum(evaluate(line, eval2) for line in data)


def eval1(expr):
    terms = expr.split()
    result = int(terms[0])
    for op, n in chunked(terms[1:], 2):
        if op == "+":
            result += int(n)
        elif op == "*":
            result *= int(n)
    return result


def eval2(expr):
    k = expr.split("*")
    return prod(eval1(e) for e in k)


def evaluate(expr, evals):
    if not "(" in expr:
        return evals(expr)

    res = {}
    parentheses_stack = deque()

    for idx, char in enumerate(expr):
        if char == "(":
            parentheses_stack.append(idx)
        elif char == ")":
            res[parentheses_stack.pop()] = idx

    a, b = next(iter(res.items()))
    e = evaluate(expr[a + 1 : b], evals)

    return evaluate(f"{expr[:a]}{e}{expr[b+1:]}", evals)


if __name__ == "__main__":
    import sys

    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("total time: {}s".format(sum(total_time)))
