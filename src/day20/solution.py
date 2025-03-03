"""solution for day 20"""

import numpy as np
from collections import defaultdict
from shortest import shortest_path


def load_data(path: str) -> tuple:
    """load the data"""
    with open(path) as f:
        data = f.read().splitlines()
    return np.array([list(row) for row in data]).astype("object")


def solve1(path):
    """solve first part"""
    data = load_data(path)
    scores, _ = shortest_path(data, traverse=False)
    shortcuts = defaultdict(int)

    # find all potential shortcuts
    for i in range(scores.shape[0] - 3):
        for j in range(scores.shape[1]):
            if (
                not np.isinf(scores[i, j])
                and np.isinf(scores[i + 1, j])
                and not np.isinf(scores[i + 2, j])
            ):
                shortcut_amount = abs(scores[i + 2, j] - scores[i, j]) - 2
                shortcuts[shortcut_amount] += 1
    for i in range(scores.shape[1] - 3):
        for j in range(scores.shape[0]):
            if (
                not np.isinf(scores[j, i])
                and np.isinf(scores[j, i + 1])
                and not np.isinf(scores[j, i + 2])
            ):
                shortcut_amount = abs(scores[j, i + 2] - scores[j, i]) - 2
                shortcuts[shortcut_amount] += 1

    total_cheats = 0
    for shortcut, num_shortcuts in shortcuts.items():
        if shortcut >= 100:
            total_cheats += num_shortcuts

    print(total_cheats)


def solve2(path):
    """solve the second part"""

    data = load_data(path)
    scores, _ = shortest_path(data, traverse=False)
    shortcuts = defaultdict(int)

    # find all potential shortcuts
    for i in range(scores.shape[0] - 3):
        for j in range(scores.shape[1]):
            if (
                not np.isinf(scores[i, j])
                and np.isinf(scores[i + 1, j])
                and not np.isinf(scores[i + 2, j])
            ):
                shortcut_amount = abs(scores[i + 2, j] - scores[i, j]) - 2
                shortcuts[shortcut_amount] += 1
    for i in range(scores.shape[1] - 3):
        for j in range(scores.shape[0]):
            if (
                not np.isinf(scores[j, i])
                and np.isinf(scores[j, i + 1])
                and not np.isinf(scores[j, i + 2])
            ):
                shortcut_amount = abs(scores[j, i + 2] - scores[j, i]) - 2
                shortcuts[shortcut_amount] += 1

    total_cheats = 0
    for shortcut, num_shortcuts in shortcuts.items():
        if shortcut >= 100:
            total_cheats += num_shortcuts

    print(total_cheats)


if __name__ == "__main__":
    solve1("data/day20/input")
