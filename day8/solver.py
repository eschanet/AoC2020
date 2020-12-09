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
    instructions = [
        (d.split(" ")[0], int(d.split(" ")[1])) for d in raw_data.strip().split("\n")
    ]
    return instructions


# PART 1
@measure_time
def solve1(data):
    return run_program(data)


# PART 2
@measure_time
def solve2(data):
    swap = {"jmp": "nop", "acc": "acc", "nop": "jmp"}
    for i, (cmd, steps) in enumerate(data):
        data[i] = swap[cmd], steps
        if run_program(data, True):
            return run_program(data, True)
        data[i] = cmd, steps


def run_program(program, only_reach_end=False):
    acc, idx = 0, 0
    visited = set()
    while (idx not in visited) and (idx < len(program)):
        visited.add(idx)
        cmd, steps = program[idx]
        idx += steps if cmd == "jmp" else 1
        acc += steps if cmd == "acc" else 0

    if only_reach_end:
        return acc if idx == len(program) else None
    else:
        return acc


if __name__ == "__main__":
    import sys

    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("total time: {}s".format(sum(total_time)))
