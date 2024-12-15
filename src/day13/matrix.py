"""module to format and then solve linear equations"""

from typing import List, Tuple
import re
import numpy as np


def format_input(
    data: List[List[str]], increment: int = 0
) -> Tuple[List[np.ndarray], List[np.ndarray]]:
    """format the input"""
    problems = []
    solutions = []
    for sublist in data:
        assert len(sublist) == 3, "sublist must always have 3 elements"
        button_a = sublist[0]
        button_b = sublist[1]
        prize = sublist[2]

        a_match = re.match(r"Button A: X\+(\d+), Y\+(\d+)", button_a)
        b_match = re.match(r"Button B: X\+(\d+), Y\+(\d+)", button_b)
        p_match = re.match(r"Prize: X=(\d+), Y=(\d+)", prize)

        problems.append(
            np.array(
                [
                    [
                        int(a_match.group(1)),
                        int(b_match.group(1)),
                    ],
                    [
                        int(a_match.group(2)),
                        int(b_match.group(2)),
                    ],
                ]
            )
        )
        solutions.append(
            np.array(
                [int(p_match.group(1)) + increment, int(p_match.group(2)) + increment]
            )
        )

    return problems, solutions


def solve_problem(problem: np.ndarray, solution: np.ndarray) -> np.ndarray:
    """solve linear eqn problem using numpy.linalg"""
    return np.linalg.solve(problem, solution)
