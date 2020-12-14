import pytest
from solver import parse, solve1, solve2

TESTDATA = """
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""

data = None


def test_parse():
    global data
    data = parse(TESTDATA)
    assert data == [
        "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
        "mem[8] = 11",
        "mem[7] = 101",
        "mem[8] = 0",
    ]


# PART 1
def test_solve1():
    solution = solve1(data)
    assert solution == 165


# PART 2
def test_solve2():
    NEWDATA = """
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
"""
    data = parse(NEWDATA)
    solution = solve2(data)
    assert solution == 208
