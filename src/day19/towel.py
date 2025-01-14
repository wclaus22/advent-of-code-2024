"""arrangement of towels to make a design via trees"""

from functools import cache


def is_possible(design: str, towels: list[str]) -> bool:
    """
    partition the design into its components by
    always removing a possible towel from the design
    thereby creating a tree of possibilities

    if a design can be fully described by a constellation
    of towels its tree will have leaf nodes that are empty
    strings (the entire design "deleted" by the towels)
    """
    return check_design(design, towels)


@cache
def check_design(design: str, towels: list[str]):
    """remove towels from a design to determine the
    children in the tree"""

    if design == "":
        return True

    children = []
    for towel in towels:
        towel_size = len(towel)
        if towel == design[:towel_size]:
            new_design = design[towel_size:]
            children.append(new_design)

    for child_design in children:
        if check_design(child_design, towels):
            return True
    return False


def count_different_ways(design: str, towels: list[str]) -> int:
    """count the different ways a design can be made"""
    return count_ways(design, towels)


@cache
def count_ways(design: str, towels: list[str]) -> int:
    """count the different ways a design can be made"""
    if design == "":
        return 1

    count = 0
    for towel in towels:
        towel_size = len(towel)
        if towel == design[:towel_size]:
            new_design = design[towel_size:]
            count += count_ways(new_design, towels)
    return count
