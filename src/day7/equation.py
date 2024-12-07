"""equation module for the day 7 solution"""

from typing import List, Callable


class Node:
    """node object for the tree data structure"""

    def __init__(self, value):
        self.value = value
        self.children = []


class EquationValidator:
    """a search tree to hold all of the possible computations
    for the given parts of the equation"""

    def __init__(self, parts, operations):
        self.root = Node(parts[0])
        _build_tree(self.root, parts[1:], operations)

    def is_valid(self, target: int) -> bool:
        """check if the target is in the tree"""
        return self._traverse(self.root, target)

    def _traverse(self, node: Node, target: int) -> bool:
        """traverse the tree to find the target"""
        if node.value is None:
            return False

        # check if leaf-node (it has no children)
        if len(node.children) == 0:
            return node.value == target

        return any(self._traverse(child, target) for child in node.children)


def _build_tree(node: Node, parts: List[int], operations: List[Callable]) -> Node:
    """build the search tree"""
    # no more parts left in the equation
    if len(parts) == 0:
        return

    new_part = parts[0]
    for operation in operations:
        node.children.append(Node(operation(node.value, new_part)))

    for child in node.children:
        _build_tree(child, parts[1:], operations)
