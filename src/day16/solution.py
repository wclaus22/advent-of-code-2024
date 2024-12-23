"""solution for day16, reindeer maze"""

import numpy as np
import pandas as pd
from dijkstra import traverse_grid, Node, backwards_traverse


def load_data(path: str):
    """load the data"""
    with open(path) as f:
        data = f.read().splitlines()
    return np.array([list(row) for row in data]).astype("object")


def solve():
    """solve both first and second parts"""
    grid = load_data("data/day16/input")

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

    tags = np.array(
        [["." for _ in range(scores.shape[1])] for _ in range(scores.shape[0])]
    ).astype("object")
    final_node = Node(x_final[0], y_final[0], ">")
    backwards_traverse(scores, tags, final_node)

    print(np.sum(tags == "O"))


if __name__ == "__main__":
    solve()
