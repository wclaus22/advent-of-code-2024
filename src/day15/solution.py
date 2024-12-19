"""solutions for day15"""

import numpy as np
from warehouse import Warehouse, get_gps


def load_data():
    """load the data"""
    with open("data/day15/input") as f:
        data = f.read().splitlines()

    split_idx = data.index("")
    grid = np.array([list(row) for row in data[:split_idx]]).astype("object")
    actions = "".join(data[split_idx + 1 :])
    return grid, actions


def solve1():
    """solve first part"""
    grid, actions = load_data()
    wh = Warehouse(grid)
    for i, action in enumerate(actions):
        wh.move_robot(action)
        print(f"Progress: {round(i/len(actions)*100,1)}%")

    final_grid = wh.grid
    gps = get_gps(final_grid)
    print(gps)


if __name__ == "__main__":
    solve1()
