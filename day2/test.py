import pytest
from solver import parse, solve1, solve2

TESTDATA = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""

data = None


def test_parse():
    global data
    data = parse(TESTDATA)
    assert data == [
        ("1", "3", "a", "abcde"),
        ("1", "3", "b", "cdefg"),
        ("2", "9", "c", "ccccccccc"),
    ]


# PART 1
def test_solve1():
    solution = solve1(data)
    assert solution == 2


# PART 2
def test_solve2():
    solution = solve2(data)
    assert solution == 1
