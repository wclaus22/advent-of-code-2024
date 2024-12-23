"""solution for day18"""

from typing import Tuple
import numpy as np


def neighbors(current: tuple, grid: np.ndarray) -> list:
    """get neighbors of current cell"""
    x, y = current
    neighbors = []
    if x > 0:
        neighbors.append((x - 1, y))
    if x < grid.shape[1] - 1:
        neighbors.append((x + 1, y))
    if y > 0:
        neighbors.append((x, y - 1))
    if y < grid.shape[0] - 1:
        neighbors.append((x, y + 1))
    return neighbors


def traverse_grid(scores: np.ndarray, grid: np.ndarray, idx) -> None:
    """backwards traverse grid"""
    grid[idx] = "O"
    current_score = scores[idx]

    valid_neighbors = []
    for neighbor in neighbors(idx, grid):
        if scores[neighbor] < current_score:
            valid_neighbors.append(neighbor)

    if len(valid_neighbors) > 0:
        traverse_grid(scores, grid, valid_neighbors[0])


def shortest_path(
    grid: np.ndarray, traverse: bool = True
) -> Tuple[np.ndarray, np.ndarray]:
    """find shortest path using dijkstras algorithm"""
    scores = np.ones_like(grid) * np.inf
    scores[0, 0] = 0
    queue = [(0, 0)]

    while len(queue) > 0:
        current = queue.pop(0)
        current_score = scores[current]
        for neighbor in neighbors(current, grid):
            if grid[neighbor] == "#":
                continue
            if current_score + 1 < scores[neighbor]:
                scores[neighbor] = current_score + 1
                queue.append(neighbor)

    if traverse:
        traverse_grid(scores, grid, (len(grid) - 1, len(grid) - 1))
    return scores, grid


def load_data(path: str) -> str:
    """load the data"""
    with open(path) as f:
        data = f.read().splitlines()
    return [tuple(map(int, item.split(","))) for item in data]


def solve1(path: str, grid_size: int, num_fallen: int):
    """solve first parts"""
    fallen_indices = load_data(path)
    grid = np.array([["." for _ in range(grid_size)] for _ in range(grid_size)]).astype(
        "object"
    )
    for fallen_idx in fallen_indices[:num_fallen]:
        grid[fallen_idx[1], fallen_idx[0]] = "#"

    _, grid = shortest_path(grid)
    print(np.sum(grid == "O"))


def solve2(path: str, grid_size: int, init_fallen: int):
    """solve the second part"""
    fallen_indices = load_data(path)

    final_idx = (grid_size - 1, grid_size - 1)
    for num_fallen in range(init_fallen, len(fallen_indices)):
        grid = np.array(
            [["." for _ in range(grid_size)] for _ in range(grid_size)]
        ).astype("object")
        for fallen_idx in fallen_indices[:num_fallen]:
            grid[fallen_idx[1], fallen_idx[0]] = "#"

        scores, _ = shortest_path(grid, traverse=False)

        # successfully reached the end if its not inf
        if scores[final_idx] == np.inf:
            print(fallen_indices[:num_fallen][-1])
            break


if __name__ == "__main__":
    solve2("data/day18/input", 71, 1024)
