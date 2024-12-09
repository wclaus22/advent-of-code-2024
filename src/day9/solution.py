"""solution for day 9"""


def load_data():
    """load the data"""
    with open("data/day9/input") as f:
        data = f.read().splitlines()
    return list(map(int, list(data[0])))


def solve1():
    """solve the first part of the problem"""

    data = load_data()

    checksum = 0

    cnt_idx = []
    cnt_free = []
    for i, num in enumerate(data):
        if i % 2 == 0:
            cnt_idx.append(num)
        else:
            cnt_free.append(num)

    pool = []
    for i, cnt in enumerate(cnt_idx):
        pool.extend([i] * cnt)

    position = 1
    current_idx = pool.pop(0)
    while len(pool) > 0:
        # change in index value in pool indicates a skip
        if pool[0] == current_idx:
            current_idx = pool.pop(0)
            checksum += position * current_idx
            position += 1
        else:
            positions_skipped = cnt_free.pop(0)
            for _ in range(positions_skipped):
                # for each skipped position, take one of the final values
                if len(pool) == 0:
                    break
                checksum += position * pool.pop(-1)
                position += 1
            if len(pool) == 0:
                break
            current_idx = pool[0]

    print(checksum)


def solve2():
    """solve the second part"""

    data = load_data()

    checksum = 0

    cnt_idx = []
    cnt_free = []
    for i, num in enumerate(data):
        if i % 2 == 0:
            cnt_idx.append(num)
        else:
            cnt_free.append(num)

    pool = []
    for i, cnt in enumerate(cnt_idx):
        pool.extend([i] * cnt)

    position = 1
    current_idx = pool.pop(0)
    while len(pool) > 0:
        # change in index value in pool indicates a skip
        if pool[0] == current_idx:
            current_idx = pool.pop(0)
            checksum += position * current_idx
            position += 1
        else:
            positions_skipped = cnt_free.pop(0)
            for _ in range(positions_skipped):
                # for each skipped position, take one of the final values
                if len(pool) == 0:
                    break
                checksum += position * pool.pop(-1)
                position += 1
            if len(pool) == 0:
                break
            current_idx = pool[0]

    print(checksum)


if __name__ == "__main__":
    solve1()
