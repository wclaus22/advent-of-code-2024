"""antinodes module"""

from typing import Dict, Tuple, List
from collections import defaultdict
import numpy as np


def get_nodes_positions(grid: np.ndarray) -> Dict[str, List[Tuple[int, int]]]:
    """get the unique nodes and their positions on the grid"""
    nodes = defaultdict(list)
    for i in range(len(grid)):
        for j in range(len(grid)):
            grid_value = grid[i, j]
            # check if valid node
            if grid_value != ".":
                nodes[grid_value].append((i, j))
    return nodes


def manhattan_distance(
    position1: Tuple[int, int], position2: Tuple[int, int]
) -> Tuple[int, int]:
    """
    figure out the manhattan distance between indices to get from one
    position to the other on the grid

    Parameters
    ----------
    position1: Tuple[int, int]
        the indices in the grid of the first position
    position2: Tuple[int, int]
        the indices in the grid of the second position

    Returns
    -------
    Tuple[int, int]
        The distance in x and y indices changes to reach position 2 from position 1
        in the manhattan (L1) distance
    """
    x1, y1 = position1
    x2, y2 = position2

    return x2 - x1, y2 - y1


def is_outside(grid: np.ndarray, position: Tuple[int, int]) -> bool:
    """check if a tuple of indices is outside the borders of the grid"""
    x, y = position
    if x < 0 or y < 0:
        return True
    if x >= grid.shape[0] or y >= grid.shape[1]:
        return True
    return False


def draw_antinodes(grid: np.ndarray) -> None:
    """draw the antinodes onto the grid"""

    nodes = get_nodes_positions(grid)
    for _, positions in nodes.items():
        for i, position_1 in enumerate(positions):
            for j, position_2 in enumerate(positions):
                if i == j:
                    continue

                diffx, diffy = manhattan_distance(position_1, position_2)

                # goto position2 and apply the manhattan distance to place the antinode
                antinode_x, antinode_y = position_2[0] + diffx, position_2[1] + diffy

                # if the antinode position is within the grid, draw the antinode
                if not is_outside(grid, (antinode_x, antinode_y)):
                    grid[antinode_x, antinode_y] = "#"


def draw_antinode(grid, position1, position2):
    """draw an antinode onto the grid"""
    if is_outside(grid, position2):
        return

    grid[position2[0], position2[1]] = "#"

    diffx, diffy = manhattan_distance(position1, position2)
    # goto position2 and apply the manhattan distance to place the antinode
    antinode_x, antinode_y = position2[0] + diffx, position2[1] + diffy

    if is_outside(grid, (antinode_x, antinode_y)):
        return

    grid[antinode_x, antinode_y] = "#"

    # keep on going with the same manhattan distance until outside of grid
    draw_antinode(grid, position2, (antinode_x, antinode_y))


def draw_antinodes_with_harmonics(grid: np.ndarray) -> None:
    """draw the antinodes but with the harmonics (the repeated application) taken into account"""

    nodes = get_nodes_positions(grid)
    for _, positions in nodes.items():
        for i, position_1 in enumerate(positions):
            for j, position_2 in enumerate(positions):
                if i == j:
                    continue

                draw_antinode(grid, position_1, position_2)
