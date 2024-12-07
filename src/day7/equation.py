"""equation module for the day 7 solution"""

from typing import List


class Node:
    """node object for the binary search tree"""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class EquationValidator:
    """a binary search tree to hold all of the possible computations
    for the given parts of the equation"""

    def __init__(self, parts):
        self.root = Node(parts[0])
        _build_binary_tree(self.root, parts[1:])

    def is_valid(self, target: int) -> bool:
        """check if the target is in the tree"""
        return self._traverse(self.root, target)

    def _traverse(self, node: Node, target: int) -> bool:
        """traverse the tree to find the target"""
        if node.value is None:
            return False

        if node.left is None and node.right is None:
            return node.value == target

        return self._traverse(node.left, target) or self._traverse(node.right, target)


def add(a, b):
    """add two numbers together"""
    return a + b


def multiply(a, b):
    """multiply two numbers together"""
    return a * b


def _build_binary_tree(node: Node, parts: List[int]) -> Node:
    """build the binary search tree"""
    if len(parts) == 0:
        return

    new_part = parts[0]
    node.left = Node(add(node.value, new_part))
    node.right = Node(multiply(node.value, new_part))

    _build_binary_tree(node.left, parts[1:])
    _build_binary_tree(node.right, parts[1:])
