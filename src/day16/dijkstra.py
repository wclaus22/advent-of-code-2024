"""module for dijkstra's algorithm"""

from typing import Literal, List, Tuple
import numpy as np


class Node:
    """node for a position on the grid"""

    def __init__(self, x: int, y: int, direction: Literal["^", "v", "<", ">"]):
        self.x = x
        self.y = y
        self.direction = direction

    def move(
        self, direction: Literal["^", "v", "<", ">"], n_steps: int = 1
    ) -> Tuple[int, int]:
        """move the node position based on the direction"""
        if direction == "^":
            return self.x - n_steps, self.y
        if direction == "v":
            return self.x + n_steps, self.y
        if direction == "<":
            return self.x, self.y - n_steps
        if direction == ">":
            return self.x, self.y + n_steps


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


def backwards_traverse(scores: np.ndarray, tags: np.ndarray, node: Node):
    """backwards traversion of the scores and updating the tags"""

    tags[node.x, node.y] = "O"
    for direction in ["^", "v", "<", ">"]:
        next_x, next_y = node.move(direction)
        current_score = scores[node.x, node.y]
        # move in same direction
        if scores[next_x, next_y] == current_score - 1:
            backwards_traverse(scores, tags, Node(next_x, next_y, direction))
        elif scores[next_x, next_y] == current_score - 1001:
            backwards_traverse(scores, tags, Node(next_x, next_y, direction))
            next_x, next_y = node.move(direction, n_steps=2)
            if scores[next_x, next_y] < current_score:
                backwards_traverse(scores, tags, Node(next_x, next_y, direction))
