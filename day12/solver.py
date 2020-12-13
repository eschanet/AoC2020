from functools import wraps
from datetime import datetime
import math

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
    return [[l[0], int(l[1:])] for l in raw_data.strip().split("\n")]


# PART 1
@measure_time
def solve1(data):
    ship = 0 + 0j
    phase = 0

    for cmd in data:
        direction = cmd[0]
        value = cmd[1]
        if direction == "F":
            ship += value * (1j) ** (phase / 90)
        elif direction in ["L", "R"]:
            phase += {"L": value, "R": -value}[direction]
        else:
            ship += pvec(direction, value)
    return (int)(abs(ship.real) + abs(ship.imag))


# PART 2
@measure_time
def solve2(data):

    ship = 0 + 0j
    waypoint = 10 + 1j
    phase = 0
    for cmd in data:
        direction = cmd[0]
        value = cmd[1]
        if direction == "F":
            ship += value * waypoint
        elif direction in ["L", "R"]:
            waypoint *= {"L": (1j) ** (value / 90), "R": (-1j) ** (value / 90)}[
                direction
            ]
        else:
            waypoint += pvec(direction, value)
    return (int)(abs(ship.real) + abs(ship.imag))


def pvec(d, m):
    return {
        "N": complex(0, m),
        "E": complex(m, 0),
        "S": complex(0, -m),
        "W": complex(-m, 0),
    }[d]


if __name__ == "__main__":
    import sys

    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("total time: {}s".format(sum(total_time)))
