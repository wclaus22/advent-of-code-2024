"""traversion module"""

import numpy as np
from collections import defaultdict


class Node:
    """node in the tree used for fragmentation"""

    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

        self.left = None
        self.right = None
        self.up = None
        self.down = None


def _is_outside(grid: np.ndarray, x: int, y: int) -> bool:
    """check if an index is outside of the grid"""

    if x < 0 or y < 0:
        return True
    if x >= grid.shape[0] or y >= grid.shape[1]:
        return True
    return False


def build_fragment(grid: np.ndarray, visited: np.ndarray, node: Node):
    """build a region of the grid interconnected by the same value"""

    visited[node.x, node.y] = True

    # check up
    if not _is_outside(grid, node.x - 1, node.y):
        if grid[node.x - 1, node.y] == node.value and not visited[node.x - 1, node.y]:
            node.up = Node(node.x - 1, node.y, node.value)
            build_fragment(grid, visited, node.up)
    # check down
    if not _is_outside(grid, node.x + 1, node.y):
        if grid[node.x + 1, node.y] == node.value and not visited[node.x + 1, node.y]:
            node.down = Node(node.x + 1, node.y, node.value)
            build_fragment(grid, visited, node.down)
    # check left
    if not _is_outside(grid, node.x, node.y - 1):
        if grid[node.x, node.y - 1] == node.value and not visited[node.x, node.y - 1]:
            node.left = Node(node.x, node.y - 1, node.value)
            build_fragment(grid, visited, node.left)
    # check right
    if not _is_outside(grid, node.x, node.y + 1):
        if grid[node.x, node.y + 1] == node.value and not visited[node.x, node.y + 1]:
            node.right = Node(node.x, node.y + 1, node.value)
            build_fragment(grid, visited, node.right)


def traverse(grid: np.ndarray, fragment: Node, indices: list, regions: dict) -> None:
    """traverse a fragment on the grid and add additional identifiers to the tile to identify
    individual regions (fragments)"""

    n_regions = regions[fragment.value]

    # remove index of node from the indices containing unfragmented candidate node indices
    idx = (fragment.x, fragment.y)
    indices.remove(idx)

    new_value = fragment.value + str(n_regions)
    grid[fragment.x, fragment.y] = new_value

    if (
        fragment.up is None
        and fragment.down is None
        and fragment.left is None
        and fragment.right is None
    ):
        return

    if fragment.up is not None:
        traverse(grid, fragment.up, indices, regions)
    if fragment.down is not None:
        traverse(grid, fragment.down, indices, regions)
    if fragment.left is not None:
        traverse(grid, fragment.left, indices, regions)
    if fragment.right is not None:
        traverse(grid, fragment.right, indices, regions)


def fragment_grid(grid: np.ndarray) -> None:
    """fragment the individual regions of the grid into their own regions"""
    indices = [(i, j) for j in range(grid.shape[1]) for i in range(grid.shape[0])]

    regions = defaultdict(int)
    visited = np.zeros(grid.shape).astype(bool)

    while len(indices) > 0:
        x, y = indices[0]
        # build the tree that allows us to fragment and annotate the region in the grid
        fragment_node = Node(x, y, grid[x, y])
        regions[grid[x, y]] += 1
        build_fragment(grid, visited, fragment_node)
        traverse(grid, fragment_node, indices, regions)
