"""solution for day two"""

from typing import List
import numpy as np


def load_data() -> List[List[int]]:
    """load the data"""
    with open("data/day2/input", "r") as f:
        data = f.read().splitlines()

    reports = []
    for item in data:
        reports.append(list(map(int, item.split(" "))))

    return reports


def is_safe(report: List[int]) -> bool:
    """
    check if a report is safe, a report is a list of levels.
    the report is safe if:

    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.
    """
    diffs = np.diff(report)
    if np.all(diffs > 0) or np.all(diffs < 0):
        if np.all(np.abs(diffs) <= 3) and np.all(np.abs(diffs) >= 1):
            return True
    return False


def is_safe_dampened(report: List[int]) -> bool:
    """
    *BRUTE FORCE SOLUTION*

    check if a report is safe, a report is a list of levels.
    the report is safe if:

    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.

    Additionally, if by removal of one level, the report is safe, then the report is safe.
    (this is the dampening condition)
    """
    for i in range(len(report)):
        if is_safe(report[:i] + report[i + 1 :]):
            return True
    return False


def solve1():
    """solve one half of the problem"""
    reports = load_data()
    n_safe_reports = 0
    for report in reports:
        if is_safe(report):
            n_safe_reports += 1
    print(n_safe_reports)


def solve2():
    """solve second half of the problem"""
    reports = load_data()
    n_safe_reports = 0
    for report in reports:
        if is_safe_dampened(report):
            n_safe_reports += 1
    print(n_safe_reports)


if __name__ == "__main__":
    solve2()
