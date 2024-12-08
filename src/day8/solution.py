"""solution for day 8"""

import numpy as np
from antinodes import draw_antinodes, draw_antinodes_with_harmonics


def load_data() -> np.ndarray:
    """load data"""
    with open("data/day8/input") as f:
        data = f.read().splitlines()
    return np.array([list(item) for item in data])


def solve1():
    """solve first part"""
    grid = load_data()
    draw_antinodes(grid)
    print(np.sum(grid == "#"))


def solve2():
    """solve second part"""
    grid = load_data()
    draw_antinodes_with_harmonics(grid)
    print(np.sum(grid == "#"))


if __name__ == "__main__":
    solve2()
