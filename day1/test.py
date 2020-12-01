import pytest
from solver import parse, solve1, solve2

TESTDATA = """
1721
979
366
299
675
1456
"""

data = None


def test_parse():
    global data
    data = parse(TESTDATA)
    assert data == [1721, 979, 366, 299, 675, 1456]


# PART 1
def test_solve1():
    solution = solve1(data)
    assert solve1([1, 2, 3, 4, 5, 6, 7]) == 1
    assert solution == 514579


# PART 2
def test_solve2():
    solution = solve2(data)
    assert solve1([1, 2, 3, 4, 5, 6, 7]) == 1
    assert solution == 241861950
