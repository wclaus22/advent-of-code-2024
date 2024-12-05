"""solution for day four"""

from typing import List
import numpy as np


def load_data() -> List[str]:
    """load the data"""
    with open("data/day4/input", "r") as f:
        data = f.read().splitlines()
    return data


def count_xmas(input_str: np.array) -> int:
    """find occurence of xmas in a string"""
    input_str = "".join(input_str)
    return input_str.count("XMAS")


def solve1():
    """solve the problem"""
    data = load_data()
    data = np.array([list(row) for row in data])

    n_xmas = 0

    # left to right and right to left
    for row in data:
        n_xmas += count_xmas(row)
        n_xmas += count_xmas(row[::-1])

    # top to bottom and bottom to top
    for i in range(len(data)):
        column = data[:, i]
        n_xmas += count_xmas(column)
        n_xmas += count_xmas(column[::-1])

    # diagonals from bottom right to top left and reverse
    tot_diagonals = 2 * len(data) - 1
    for i in range(tot_diagonals):
        diag = np.diagonal(data, offset=i - len(data))
        n_xmas += count_xmas(diag)
        n_xmas += count_xmas(diag[::-1])
        diag_rotated = np.diagonal(np.rot90(data), offset=i - len(data))
        n_xmas += count_xmas(diag_rotated)
        n_xmas += count_xmas(diag_rotated[::-1])

    print(n_xmas)


def solve2():
    """solve the second half of the problem"""
    data = load_data()
    data = np.array([list(row) for row in data])

    n_mas = 0
    for i in range(len(data) - 2):
        for j in range(len(data) - 2):
            submatrix = data[i : i + 3, j : j + 3]
            diag1 = "".join([submatrix[0, 0], submatrix[1, 1], submatrix[2, 2]])
            diag2 = "".join([submatrix[2, 0], submatrix[1, 1], submatrix[0, 2]])

            mas_1 = diag1 in ("MAS", "SAM")
            mas_2 = diag2 in ("MAS", "SAM")
            if mas_1 and mas_2:
                n_mas += 1

    print(n_mas)


if __name__ == "__main__":
    solve1()
    solve2()
