"""solution for day19"""

from towel import is_possible, count_different_ways


def load_data(path: str) -> tuple:
    """load the data"""
    with open(path) as f:
        data = f.read().splitlines()
    split_idx = data.index("")
    towels = data[split_idx - 1].replace(" ", "").split(",")
    designs = data[split_idx + 1 :]

    return towels, designs


def solve1(path: str):
    """solve first part of the challenge
    (only check if the designs are possible)"""
    towels, designs = load_data(path)
    cnt = 0
    for design in designs:
        if is_possible(design, tuple(towels)):
            cnt += 1
    print(cnt)


def solve2(path: str):
    """solve second part of the challenge
    (count the different ways a design can be made)"""
    towels, designs = load_data(path)
    cnt = 0
    for design in designs:
        cnt += count_different_ways(design, tuple(towels))
    print(cnt)


if __name__ == "__main__":
    solve2("data/day19/input")
