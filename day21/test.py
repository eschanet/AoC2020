import pytest
from solver import parse, solve1, solve2

TESTDATA = """
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
"""

data = None


def test_parse():
    global data
    data = parse(TESTDATA)
    assert data == (
        {
            "dairy": {"mxmxvkd"},
            "fish": {"mxmxvkd", "sqjhc"},
            "soy": {"sqjhc", "fvjkl"},
        },
        [
            "mxmxvkd",
            "kfcds",
            "sqjhc",
            "nhms",
            "trh",
            "fvjkl",
            "sbzzf",
            "mxmxvkd",
            "sqjhc",
            "fvjkl",
            "sqjhc",
            "mxmxvkd",
            "sbzzf",
        ],
    )


# PART 1
def test_solve1():
    solution = solve1(data)
    assert solution == 5


# PART 2
def test_solve2():
    solution = solve2(data)
    assert solution == "mxmxvkd,sqjhc,fvjkl"
