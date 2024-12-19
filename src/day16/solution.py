"""solution for day16, reindeer maze"""

import numpy as np
import pandas as pd
from dijkstra import traverse_grid, Node


def load_data(path: str):
    """load the data"""
    with open(path) as f:
        data = f.read().splitlines()
    return np.array([list(row) for row in data]).astype("object")


def solve1():
    """solve first part"""
    grid = load_data("data/day16/test2")

    x_init, y_init = np.where(grid == "S")

    root = Node(x_init[0], y_init[0], direction=">")
    scores = np.ones_like(grid) * np.inf
    directions = np.array(
        [["." for _ in range(scores.shape[1])] for _ in range(scores.shape[0])]
    ).astype("object")
    traverse_grid(grid, scores, directions, root)

    x_final, y_final = np.where(grid == "E")
    print(scores[x_final, y_final])
    print(pd.DataFrame(scores))
    print(pd.DataFrame(directions))

    # breakpoint()
    # tags = np.ones_like(grid).astype("object")
    # backwards_traverse(scores)


if __name__ == "__main__":
    solve1()
