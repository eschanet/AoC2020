from functools import wraps
from datetime import datetime
import re
from collections import defaultdict, deque

total_time = []


def measure_time(func):
    @wraps(func)
    def _func(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        total_time.append((end - start).total_seconds())
        return result

    return _func


class ChildBag:
    def __init__(self, color, count):
        self.color = color
        self.count = count


@measure_time
def parse(raw_data):
    data = raw_data.strip().split("\n")

    conts = defaultdict(list)
    contd_in = defaultdict(list)

    for line in data:
        # get all children bags
        children = re.findall(r"(\d) (\w+ \w+)", line)
        # name of parent bag is two words wide
        parentBag = " ".join(line.split()[:2])
        for count, color in children:
            contd_in[color].append(parentBag)
            conts[parentBag].append(ChildBag(color, int(count)))

    return (contd_in, conts)


# PART 1
@measure_time
def solve1(data):
    contd_in = data[0]

    def bfs(gr, color):
        color_contd = set()
        q = deque([color])  # never used double-ended queue before ...
        while q:
            u = q.popleft()
            for v in gr[u]:
                if not v in color_contd:
                    color_contd.add(v)
                    q.append(v)
        return color_contd

    return len(bfs(contd_in, "shiny gold"))


# PART 2
@measure_time
def solve2(data):
    conts = data[1]

    # oh boy, here we go again, hope this doesn't go too deep
    def bag_weight(color):
        w = 0
        for child in conts[color]:
            w += child.count * (1 + bag_weight(child.color))
        return w

    return bag_weight("shiny gold")


if __name__ == "__main__":
    import sys

    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("total time: {}s".format(sum(total_time)))
