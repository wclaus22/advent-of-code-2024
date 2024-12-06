"""solution for day 6"""

import sys
import copy
from typing import Tuple
import numpy as np

from guard import Guard


def load_data():
    """load data from file"""
    with open("data/day6/input") as f:
        data = f.read().splitlines()
    return np.array([list(x) for x in data])


def find_initial_position(data) -> Tuple[int, int]:
    """find the initial position of the guard"""
    x, y = np.where(data == "^")
    return x[0], y[0]


def draw(grid, guard) -> None:
    """draw the positions on the grid"""

    x_ahead, y_ahead = guard.look_ahead()
    if x_ahead < 0 or y_ahead < 0:
        grid[guard.position] = "X"
        return
    if x_ahead >= grid.shape[0] or y_ahead >= grid.shape[1]:
        grid[guard.position] = "X"
        return
    if grid[x_ahead, y_ahead] == "#":
        guard.rotate()
        draw(grid, guard)
    else:
        grid[guard.position] = "X"
        guard.move()
        draw(grid, guard)


def solve1(data: np.ndarray, limit=10000) -> int:
    """solve the first part"""
    initial_position = find_initial_position(data)
    guard = Guard(initial_position=initial_position, initial_direction="up")
    sys.setrecursionlimit(limit)
    draw(data, guard)

    return np.sum(data == "X")


def solve2():
    """solve the second part"""
    data = load_data()

    n_possibilities = 0
    # brute force solution
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            # if starting position or already an obstruction, skip the position
            if data[i, j] in ("^", "#"):
                continue
            n_possibilities += 1

    n_loop_possibities = 0
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            # if starting position or already an obstruction, skip the position
            if data[i, j] in ("^", "#"):
                continue
            # try the position
            print(
                f"Trying position {round(i/data.shape[0]*100, 1)}%, "
                + f"{round(j/data.shape[1]*100, 1)}%"
            )
            data_copy = copy.deepcopy(data)
            data_copy[i, j] = "#"
            # if the recursion limit is reached, the position is assumed to be in a loop
            try:
                solve1(data_copy, n_possibilities)
            except RecursionError:
                print(f"Position {i, j} is in a loop")
                n_loop_possibities += 1

    print("Solution:", n_loop_possibities)


if __name__ == "__main__":
    solve2()
