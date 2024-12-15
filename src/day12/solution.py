"""solution for day12"""

import numpy as np
from collections import defaultdict

from fragments import fragment_grid, _is_outside


def load_data():
    """load the data"""
    with open("data/day12/test") as f:
        data = f.read().splitlines()
    return np.array([list(row) for row in data], dtype="object")


def _add_perimeter(grid: np.ndarray, perimeter: dict, tile: int, x, y) -> None:
    """adding a perimeter logic to the perimeter dict"""
    if _is_outside(grid, x, y):
        perimeter[tile] += 1
    else:
        if tile != grid[x, y]:
            perimeter[tile] += 1


def solve1():
    """solve first part"""
    data = load_data()

    fragment_grid(data)

    area = defaultdict(int)
    perimeter = defaultdict(int)
    for i, row in enumerate(data):
        for j, tile in enumerate(row):
            area[tile] += 1

            # check up
            _add_perimeter(data, perimeter, tile, i - 1, j)
            # check down
            _add_perimeter(data, perimeter, tile, i + 1, j)
            # check left
            _add_perimeter(data, perimeter, tile, i, j - 1)
            # check right
            _add_perimeter(data, perimeter, tile, i, j + 1)

    total_price = 0
    for tile, area_value in area.items():
        print(tile, area_value, perimeter[tile], area_value * perimeter[tile])
        total_price += area_value * perimeter[tile]

    print(total_price)


def solve2():
    """solve the second part"""
    data = load_data()

    fragment_grid(data)

    area = defaultdict(int)
    for i, row in enumerate(data):
        for j, tile in enumerate(row):
            area[tile] += 1

    sides = defaultdict(int)
    total_price = 0
    for tile, area_value in area.items():
        print(tile, area_value, sides[tile], area_value * sides[tile])
        total_price += area_value * sides[tile]

    print(total_price)


if __name__ == "__main__":
    solve1()
