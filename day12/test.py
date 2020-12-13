import pytest
from solver import parse, solve1, solve2

TESTDATA = """
F10
N3
F7
R90
F11
"""

data = None


def test_parse():
    global data
    data = parse(TESTDATA)
    assert data == [
        ["F", 10],
        ["N", 3],
        ["F", 7],
        ["R", 90],
        ["F", 11],
    ]


# PART 1
def test_solve1():
    solution = solve1(data)
    assert solution == 25


# PART 2
def test_solve2():
    solution = solve2(data)
    assert solution == 286
