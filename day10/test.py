import pytest
from solver import parse, solve1, solve2

TESTDATA = """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""

data = None


def test_parse():
    global data
    data = parse(TESTDATA)
    assert data == [
        28,
        33,
        18,
        42,
        31,
        14,
        46,
        20,
        48,
        47,
        24,
        23,
        49,
        45,
        19,
        38,
        39,
        11,
        1,
        32,
        25,
        35,
        8,
        17,
        7,
        9,
        4,
        2,
        34,
        10,
        3,
    ]


# PART 1
def test_solve1():
    solution = solve1(data)
    assert solution == 220


# PART 2
def test_solve2():
    solution = solve2(data)
    assert solution == 19208
