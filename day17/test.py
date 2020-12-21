import pytest
from solver import parse, solve1, solve2

TESTDATA = """
.#.
..#
###
"""

data = None


def test_parse():
    global data
    data = parse(TESTDATA)
    assert data == 


# PART 1
def test_solve1():
    solution = solve1(data)
    assert solution == 112


# PART 2
def test_solve2():
    solution = solve2(data)
    assert solution == 848
