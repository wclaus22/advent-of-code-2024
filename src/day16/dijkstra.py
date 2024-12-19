"""module for dijkstra's algorithm"""

from typing import Literal, List, Tuple
import numpy as np


class Node:
    """node for a position on the grid"""

    def __init__(self, x: int, y: int, direction: Literal["^", "v", "<", ">"]):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self, direction: Literal["^", "v", "<", ">"]) -> Tuple[int, int]:
        """move the node position based on the direction"""
        if direction == "^":
            return self.x - 1, self.y
        if direction == "v":
            return self.x + 1, self.y
        if direction == "<":
            return self.x, self.y - 1
        if direction == ">":
            return self.x, self.y + 1


def get_valid_directions(direction: Literal["^", "v", "<", ">"]) -> List[str]:
    """get the valid directions, one can never go back"""
    if direction == ">":
        return [">", "^", "v"]
    if direction == "<":
        return ["<", "^", "v"]
    if direction == "^":
        return ["^", "<", ">"]
    if direction == "v":
        return ["v", "<", ">"]


def get_adjacent_nodes(grid: np.ndarray, node: Node) -> Tuple[List[Node], List[int]]:
    """return the adjacent nodes"""

    next_nodes = []
    weights = []
    next_directions = get_valid_directions(node.direction)
    for next_direction in next_directions:
        new_x, new_y = node.move(next_direction)
        new_grid_value = grid[new_x, new_y]

        # dont allow moving into walls
        if new_grid_value == "#":
            continue

        new_weight = 1

        # turning 90 degrees costs 1000 extra
        if node.direction != next_direction:
            new_weight += 1000

        weights.append(new_weight)
        next_nodes.append(Node(new_x, new_y, direction=next_direction))

    return next_nodes, weights


def traverse_grid(
    grid: np.ndarray, scores: np.ndarray, directions: np.ndarray, root: Node
):
    """traverse the grid"""
    scores[root.x, root.y] = 0
    directions[root.x, root.y] = root.direction
    queue = [root]

    while len(queue) > 0:

        node = queue.pop(0)
        node_score = scores[node.x, node.y]
        node.direction = directions[node.x, node.y]
        next_nodes, next_weights = get_adjacent_nodes(grid, node)

        # order next nodes based on score
        selected_nodes = []
        for node, weight in zip(next_nodes, next_weights):
            new_node_score = node_score + weight
            if new_node_score < scores[node.x, node.y]:
                scores[node.x, node.y] = new_node_score
                directions[node.x, node.y] = node.direction
                selected_nodes.append(node)

        indices = np.argsort([scores[node.x, node.y] for node in selected_nodes])
        for i in indices:
            queue.append(selected_nodes[i])
