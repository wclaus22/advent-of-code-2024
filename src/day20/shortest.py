"""find the shortest path using dijkstras algorithm"""

from typing import Tuple
import numpy as np
from numpy.typing import NDArray


def neighbors(current: tuple, grid: NDArray) -> list:
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


def traverse_grid(scores: NDArray, grid: NDArray, idx: Tuple[int, int]) -> None:
    """backwards traverse grid"""
    grid[idx] = "O"
    current_score = scores[idx]

    valid_neighbors = []
    for neighbor in neighbors(idx, grid):
        if scores[neighbor] < current_score:
            valid_neighbors.append(neighbor)

    if len(valid_neighbors) > 0:
        traverse_grid(scores, grid, valid_neighbors[0])


def shortest_path(grid: NDArray, traverse: bool = True) -> Tuple[NDArray, NDArray]:
    """find shortest path using dijkstras algorithm"""
    init_x, init_y = np.where(grid == "S")
    init = (init_x[0], init_y[0])
    scores = np.ones_like(grid) * np.inf
    scores[init] = 0
    queue = [init]

    while len(queue) > 0:
        current = queue.pop(0)
        current_score = scores[current]
        for neighbor in neighbors(current, grid):
            if grid[neighbor] == "#":
                continue
            if grid[neighbor] == "E":
                scores[neighbor] = current_score + 1
                break
            if current_score + 1 < scores[neighbor]:
                scores[neighbor] = current_score + 1
                queue.append(neighbor)

    if traverse:
        final_x, final_y = np.where(grid == "E")
        traverse_grid(
            scores,
            grid,
            (final_x[0], final_y[0]),
        )

    return scores, grid
