"""solution for day 10"""

import numpy as np
from path import build_path, Node, traverse


def load_data() -> np.ndarray:
    """load the data"""
    with open("data/day10/input") as f:
        data = f.read().splitlines()
    return np.array([list(map(int, list(row))) for row in data])


def solve():
    """solve both parts of the problem"""
    grid = load_data()

    total_score = 0
    total_rating = 0
    starting_x, starting_y = np.where(grid == 0)
    for x, y in zip(starting_x, starting_y):
        unique_final_positions = set()
        all_final_positions = []

        init_node = Node(x, y, grid[x, y])
        build_path(grid, init_node)
        traverse(init_node, unique_final_positions, all_final_positions)

        total_score += len(unique_final_positions)
        total_rating += len(all_final_positions)

    print(total_score)
    print(total_rating)


if __name__ == "__main__":
    solve()
