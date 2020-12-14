from functools import wraps
from datetime import datetime
import re

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
    return solve(data)


# PART 2
@measure_time
def solve2(data):
    return solve(data, floating_bits=True)


def solve(data, floating_bits=False):

    memory = dict()  # memory I'm writing to
    masks = list()  # list of masks used for part2
    ones, zeros = 0, 2 ** 35  # 36-bit masks!

    for line in data:
        mask = re.findall(r"mask = ([X01]+)", line)
        if mask:
            zeros = int(re.sub("X", "1", mask[0]), 2)
            ones = int(re.sub("X", "0", mask[0]), 2)
            if floating_bits:
                masks = create_masks(mask[0])
            continue
        match = re.findall(r"mem\[(\d+)\] = (\d+)", line)
        if match:
            addr, value = map(int, match[0])
            if not floating_bits:
                # apply mask to value
                # just need to bitwise 'and' with the zeros
                # and bitwise 'or' with the ones
                memory[addr] = (value & zeros) | ones
            else:
                # in case of the floating bits, we are not overwriting
                # the values, but the actual addresses.
                #
                # Previously built an entire list of all masks that we need to apply

                for mask in masks:
                    # bitwise 'or' for the ones (as they overwrite existing bit),
                    # nothing to do for zeros.
                    # for the floating bits: split into ones and zeros, each
                    # overwriting the corresponding address bit.
                    target_addr = ((addr | ones) & mask[0]) | mask[1]
                    memory[target_addr] = value

    return sum(memory.values())


def create_masks(mask):
    def get_binary(n, bits):
        return bin(n)[2:].zfill(bits)

    # create all needed masks for a given number of floating bits
    masks = list()
    count = mask.count("X")
    # 2 possibilities for each #, i.e. 2**N possibilities for N pounds.
    # each possible mask variation can be uniquely defined by a binary number
    # from 0 to 2**N
    for index in range(2 ** count):
        # using pound as a placeholder for bits to vary around
        newmask = re.sub("[01]", "#", mask)
        for d in get_binary(index, count):
            newmask = newmask.replace("X", d, 1)
        zeros = int(re.sub("#", "1", newmask), 2)
        ones = int(re.sub("#", "0", newmask), 2)
        masks.append((zeros, ones))
    return masks


if __name__ == "__main__":
    import sys

    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("total time: {}s".format(sum(total_time)))
