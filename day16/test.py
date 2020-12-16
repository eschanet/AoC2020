import pytest
from solver import parse, solve1, solve2

TESTDATA = """
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""

data = None


def test_parse():
    global data
    data = parse(TESTDATA)
    assert data == {
        "ticket_rules": {
            "class": {1, 2, 3, 5, 6, 7},
            "row": {
                6,
                7,
                8,
                9,
                10,
                11,
                33,
                34,
                35,
                36,
                37,
                38,
                39,
                40,
                41,
                42,
                43,
                43,
                44,
            },
            "seat": {
                13,
                14,
                15,
                16,
                17,
                18,
                19,
                20,
                21,
                22,
                23,
                24,
                25,
                26,
                27,
                28,
                29,
                30,
                31,
                32,
                33,
                34,
                35,
                36,
                37,
                38,
                39,
                40,
                45,
                46,
                47,
                48,
                49,
                50,
            },
        },
        "my_ticket": [7, 1, 14],
        "nearby_tickets": [
            [7, 3, 47],
            [40, 4, 50],
            [55, 2, 20],
            [38, 6, 12],
        ],
    }


# PART 1
def test_solve1():
    solution = solve1(data)
    assert solution == 71


# PART 2
def test_solve2():
    solution = solve2(data)
    assert solution == 1
