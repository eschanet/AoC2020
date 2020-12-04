from functools import wraps
from datetime import datetime
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
    # could this be ANY uglier?
    passports = [
        {d.split(":")[0]: d.split(":")[1] for d in passport}
        for passport in [
            d.replace("\n", " ").split(" ") for d in raw_data.strip().split("\n\n")
        ]
    ]
    return passports


# PART 1
@measure_time
def solve1(data):
    needed_keys = ["byr", "iyr", "iyr", "hgt", "hcl", "ecl", "pid"]
    valid_passports = [
        passport for passport in data if all(key in passport for key in needed_keys)
    ]
    return len(valid_passports)


# PART 2
@measure_time
def solve2(data):
    valid_passports = [passport for passport in data if valid_passport(passport)]
    return len(valid_passports)


def valid_passport(
    passport,
    needed_keys=["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"],
    optional_keys=["cid"],
):

    if not all(key in passport for key in needed_keys):
        return False

    if "byr" in needed_keys:
        # define some rules for birth year
        if not (
            re.match(r"^\d{4}$", passport["byr"])
            and int(passport["byr"]) >= 1920
            and int(passport["byr"]) <= 2002
        ):
            return False

    if "iyr" in needed_keys:
        # define some rules for issue year
        if not (
            re.match(r"^\d{4}$", passport["iyr"])
            and int(passport["iyr"]) >= 2010
            and int(passport["iyr"]) <= 2020
        ):
            return False

    if "eyr" in needed_keys:
        # define some rules for expiry year
        if not (
            re.match(r"^\d{4}$", passport["eyr"])
            and int(passport["eyr"]) >= 2020
            and int(passport["eyr"]) <= 2030
        ):
            return False

    if "hgt" in needed_keys:
        # define some rules for height
        if not (re.match(r"\d*(cm|in)", passport["hgt"])):
            return False

        height = int(passport["hgt"][:-2])
        if "cm" in passport["hgt"][-2:]:
            if not (height >= 150 and height <= 193):
                return False
        if "in" in passport["hgt"][-2:]:
            if not (height >= 59 and height <= 76):
                return False

    if "ecl" in needed_keys:
        # define some rules for eye colour
        if not passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False

    if "pid" in needed_keys:
        # define some rules for passport id
        if not re.match(r"^\d{9}$", passport["pid"]):
            return False

    if "hcl" in needed_keys:
        # define some rules for hair colour
        if not re.match(r"^#[a-f0-9]{6}$", passport["hcl"]):
            return False

    # no rules flagged it as invalid, so must be valid
    return True


if __name__ == "__main__":
    import sys

    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("total time: {}s".format(sum(total_time)))
