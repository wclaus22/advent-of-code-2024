"""operations module"""


def add(a: int, b: int) -> int:
    """add two numbers together"""
    return a + b


def multiply(a: int, b: int) -> int:
    """multiply two numbers together"""
    return a * b


def concatenate(a: int, b: int) -> int:
    """concatenate two numbers to make a new number"""
    return int(str(a) + str(b))
