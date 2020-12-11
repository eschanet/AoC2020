import pytest
import copy
from solver import parse, solve1, solve2

TESTDATA = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""

data = None


def test_parse():
    global data
    data = parse(TESTDATA)
    # asserts go here


# PART 1
def test_solve1():
    my_data = copy.deepcopy(data)
    solution = solve1(my_data)
    assert solution == 37


# PART 2
def test_solve2():
    my_data = copy.deepcopy(data)
    solution = solve2(my_data)
    assert solution == 26
