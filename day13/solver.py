from functools import wraps
import toolz
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
    timestamp = int(raw_data.strip().split("\n")[0])
    busses = [
        (i, int(bus))
        for i, bus in enumerate(raw_data.strip().split("\n")[1].split(","))
        if bus != "x"
    ]
    return (timestamp, busses)


# PART 1
@measure_time
def solve1(data):
    t, busses = data[0], data[1]
    nearest_bus, smallest_diff = 0, None

    for i, b in busses:
        d = b - (t % b)
        if not smallest_diff or d < smallest_diff:
            smallest_diff, nearest_bus = d, b
    return nearest_bus * smallest_diff


# PART 2
@measure_time
def solve2(data):
    busses = data[1]
    return crt(busses)


def get_timestamp(busses):
    p, t = 1, 0

    for dt, bus in busses:
        while True:
            if (dt + t) % bus == 0:
                break
            t += p
        p *= bus
    return t


def crt(busses):
    # Problem I want to solve:
    # Find x such that for all i:
    #      x + offset_i = 0 (mod busID_i)
    #   => x = -offset_i (mod busID_i) = busID_i + offset_i (mod busID_i)
    #
    # All bus IDs are prime, so use chinese remainder theorem to solve:
    #      x = sum_i  (m_i-r_i) * N_i * s_i
    # where m_i = busID_i (the modulus), r_i = offset_i, N = m_1 * m_2 * ... * m_n,
    # N_i = N / m_i and finally s_i is the inverse of N_i mod m_i, i.e. s_i * N_i = 1 (mod m_i)

    N = toolz.reduce(
        lambda a, b: a * b, map(toolz.last, busses)
    )  # product of all moduli (the bus numbers)

    return sum((m - r) * N // m * pow(N // m, -1, m) for r, m in busses) % N


if __name__ == "__main__":
    import sys

    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("total time: {}s".format(sum(total_time)))
