import pytest
from solver import parse, solve1, solve2, ChildBag

TESTDATA = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

data = None


def test_parse():
    global data
    data = parse(TESTDATA)
    print(data)
    assert data[0] == {
        "bright white": ["light red", "dark orange"],
        "muted yellow": ["light red", "dark orange"],
        "shiny gold": ["bright white", "muted yellow"],
        "faded blue": ["muted yellow", "dark olive", "vibrant plum"],
        "dark olive": ["shiny gold"],
        "vibrant plum": ["shiny gold"],
        "dotted black": ["dark olive", "vibrant plum"],
    }


# PART 1
def test_solve1():
    solution = solve1(data)
    assert solution == 4


# PART 2
def test_solve2():
    solution = solve2(data)
    assert solution == 32
