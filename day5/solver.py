from functools import wraps
from datetime import datetime
import math
import numpy as np

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
    data = raw_data.strip().split("\n")
    return data


# PART 1
@measure_time
def solve1(data):
    seatIDs = [get_seatID(code) for code in data]
    return max(seatIDs)


# PART 2
@measure_time
def solve2(data):
    maxSeatID = 128 * 8 + 8
    seatIDs = [get_seatID(code) for code in data]
    missingIDs = [seatID for seatID in range(maxSeatID) if not seatID in seatIDs]
    for missingID in missingIDs:
        if (missingID - 1 in seatIDs) and (missingID + 1 in seatIDs):
            return missingID


def get_seatID(code, rows=128, columns=8):
    n_iter_rows = int(math.log2(rows))
    n_iter_columns = int(math.log2(columns))
    coordinates = np.array(
        [[(row, column) for column in range(columns)] for row in range(rows)]
    )
    for x_idx in range(n_iter_rows):
        rows = int(rows / 2)
        byte = str(code[x_idx])
        if byte == "F":
            coordinates = coordinates[0:rows, :, :]
        if byte == "B":
            coordinates = coordinates[rows:, :, :]

    for y_idx in range(x_idx + 1, x_idx + 1 + n_iter_columns):
        columns = int(columns / 2)
        byte = str(code[y_idx])
        if byte == "L":
            coordinates = coordinates[:, 0:columns, :]
        if byte == "R":
            coordinates = coordinates[:, columns:, :]

    column = int(coordinates[0, 0, 0])
    row = int(coordinates[0, 0, 1])
    return column * 8 + row


if __name__ == "__main__":
    import sys

    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("total time: {}s".format(sum(total_time)))
