import pytest
from solver import parse, solve1, solve2

TESTDATA = """
1 + (2 * 3) + (4 * (5 + 6))
"""

data = None


def test_parse():
    global data
    data = parse(TESTDATA)
    assert data == ["1 + (2 * 3) + (4 * (5 + 6))"]


# PART 1
def test_solve1():
    solution = solve1(data)
    assert solution == 51


# PART 2
def test_solve2():
    solution = solve2(data)
    assert solution == 51
