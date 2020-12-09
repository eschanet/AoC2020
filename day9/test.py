import pytest
from solver import parse, solve1, solve2

TESTDATA = """
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""

data = None


def test_parse():
    global data
    data = parse(TESTDATA)
    assert data == [
        35,
        20,
        15,
        25,
        47,
        40,
        62,
        55,
        65,
        95,
        102,
        117,
        150,
        182,
        127,
        219,
        299,
        277,
        309,
        576,
    ]


# PART 1
def test_solve1():
    solution = solve1(data, 5)
    assert solution == 127


# PART 2
def test_solve2():
    solution = solve2(data, solve1(data, 5))
    assert solution == 62
