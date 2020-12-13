import pytest
from solver import parse, solve1, solve2

TESTDATA = """
939
7,13,x,x,59,x,31,19
"""

data = None


def test_parse():
    global data
    data = parse(TESTDATA)
    assert data == (939, [(0, 7), (1, 13), (4, 59), (6, 31), (7, 19)])


# PART 1
def test_solve1():
    solution = solve1(data)
    assert solution == 295


# PART 2
def test_solve2():
    solution = solve2(data)
    assert solution == 1068781
