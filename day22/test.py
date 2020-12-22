import pytest
from solver import parse, solve1, solve2

TESTDATA = """
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""

data = None


def test_parse():
    global data
    data = parse(TESTDATA)
    # asserts go here


# PART 1
def test_solve1():
    solution = solve1(data)
    assert solution == 306


# PART 2
def test_solve2():
    solution = solve2(data)
    assert solution == 291
