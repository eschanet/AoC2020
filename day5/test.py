import pytest
from solver import parse, solve1, solve2

TESTDATA = """
FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
"""

data = None


def test_parse():
    global data
    data = parse(TESTDATA)
    assert data == [
        "FBFBBFFRLR",
        "BFFFBBFRRR",
        "FFFBBBFRRR",
        "BBFFBBFRLL",
    ]


# PART 1
def test_solve1():
    solution = solve1(data)
    assert solution == 820


# PART 2
def test_solve2():
    solution = solve2(data)
    # Can't do a test for this one unless I build my own input... :-(
    # assert solution == 357
