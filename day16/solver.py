from functools import wraps
from datetime import datetime
import pandas as pd
import re

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


@measure_time
def parse(raw_data):
    data = {}
    parts = raw_data.strip().split("\n\n")

    ticket_rules = {
        range.split(":")[0]: re.findall(r"[0-9]+", range)
        for range in parts[0].split("\n")
    }
    for val, rg in ticket_rules.items():
        rg = list(map(int, rg))
        ticket_rules[val] = set(
            list(range(rg[0], rg[1] + 1)) + list(range(rg[2], rg[3] + 1))
        )

    data["ticket_rules"] = ticket_rules
    data["my_ticket"] = list(map(int, parts[1].split("\n")[1].split(",")))
    data["nearby_tickets"] = [
        list(map(int, ticket.split(","))) for ticket in parts[2].split("\n")[1:]
    ]

    return data


# PART 1
@measure_time
def solve1(data):
    allowed_numbers = set.union(*[rule for val, rule in data["ticket_rules"].items()])
    forbidden = [
        n
        for ticket in data["nearby_tickets"]
        for n in ticket
        if n not in allowed_numbers
    ]

    return sum(forbidden)


# PART 2
@measure_time
def solve2(data):
    allowed_numbers = set.union(*[rule for val, rule in data["ticket_rules"].items()])
    allowed_tickets = [
        ticket
        for ticket in data["nearby_tickets"]
        if all(n in allowed_numbers for n in ticket)
    ]

    allowed = pd.DataFrame(
        data=True,
        columns=range(len(data["ticket_rules"].keys())),
        index=data["ticket_rules"].keys(),
    )
    for rule_name, allowed_range in data["ticket_rules"].items():
        for i_field in range(len(data["ticket_rules"].keys())):
            for ticket in allowed_tickets:
                if ticket[i_field] not in allowed_range:
                    allowed.loc[rule_name, i_field] = False

    result = 1
    my_ticket = data["my_ticket"]
    while allowed.sum(axis=1).max() > 1:
        for name, row in allowed[allowed.sum(axis=1) == 1].iterrows():
            if name.startswith("departure"):
                result *= my_ticket[row[row].index[0]]
            allowed.loc[:, row[row].index[0]] = False
    return result


if __name__ == "__main__":
    import sys

    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("total time: {}s".format(sum(total_time)))
