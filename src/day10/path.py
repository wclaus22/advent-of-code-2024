"""path and node module for day10"""

from typing import Literal
import numpy as np


class Node:
    """Node class"""

    def __init__(self, x: int, y: int, value: int):
        self.x = x
        self.y = y
        self.value = value

        self.left = None
        self.right = None
        self.up = None
        self.down = None


def _is_outside(grid: np.ndarray, x: int, y: int) -> bool:
    """check if position is outside of the grid"""
    if x < 0 or y < 0:
        return True
    if x >= grid.shape[0] or y >= grid.shape[1]:
        return True
    return False


def set_node(
    grid: np.ndarray,
    node: Node,
    new_x: int,
    new_y: int,
    direction: Literal["up", "down", "left", "right"],
) -> None:
    """set node onto new position"""
    if not _is_outside(grid, new_x, new_y):
        # only a single increment constitutes to a valid hiking path
        new_value = grid[new_x, new_y]
        if grid[new_x, new_y] == node.value + 1:
            setattr(node, direction, Node(new_x, new_y, new_value))


def build_path(grid: np.ndarray, node: Node):
    """build the path into a tree"""

    set_node(grid, node, node.x - 1, node.y, "up")
    set_node(grid, node, node.x + 1, node.y, "down")
    set_node(grid, node, node.x, node.y - 1, "left")
    set_node(grid, node, node.x, node.y + 1, "right")

    if node.up is not None:
        build_path(grid, node.up)
    if node.down is not None:
        build_path(grid, node.down)
    if node.left is not None:
        build_path(grid, node.left)
    if node.right is not None:
        build_path(grid, node.right)


def traverse(node, final_positions: set, all_positions: list):
    """traverse the tree to find the unique final positions
    and separate paths that lead to the final height"""
    # if in final position add it to the set of unique positions
    if node.value == 9:
        final_positions.add((node.x, node.y))
        all_positions.append((node.x, node.y))

    if (
        node.up is None
        and node.down is None
        and node.left is None
        and node.right is None
    ):
        return

    if node.up is not None:
        traverse(node.up, final_positions, all_positions)
    if node.down is not None:
        traverse(node.down, final_positions, all_positions)
    if node.left is not None:
        traverse(node.left, final_positions, all_positions)
    if node.right is not None:
        traverse(node.right, final_positions, all_positions)
