"""solution for day 20"""

from typing import Tuple
import numpy as np
from numpy.typing import NDArray
from collections import defaultdict

from shortest import shortest_path, is_valid, neighbors


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
    start_x, start_y = np.where(data == "S")
    scores, _ = shortest_path(data, traverse=False)
    total_cheats_above_cutoff = 0
    total_moves = 20
    cutoff = 100
    all_amounts = defaultdict(int)

    current_score = 0
    current_position = (start_x[0], start_y[0])
    _neighbors = neighbors(current_position, scores)
    candidates = _neighbors
    new_num_cheats, amounts = search_diamond(
        current_position, total_moves, scores, cutoff
    )
    total_cheats_above_cutoff += new_num_cheats
    all_amounts.update(amounts)

    while len(candidates) > 0:
        candidate = candidates.pop()

        if not np.isinf(scores[candidate]) and scores[candidate] > current_score:
            current_score = scores[candidate]
            new_num_cheats, amounts = search_diamond(
                candidate, total_moves, scores, cutoff
            )
            all_amounts.update(amounts)
            total_cheats_above_cutoff += new_num_cheats
            _neighbors = neighbors(candidate, scores)
            candidates.extend(_neighbors)

    print(total_cheats_above_cutoff)


def search_diamond(
    current_position: Tuple[int, int], size: int, grid: NDArray, cutoff: int
) -> int:
    """search a diamond shape from the current position in the grid"""
    x, y = current_position
    amounts = defaultdict(int)

    tot_added_cheats = 0
    for i in range(1, size + 1):
        for dy in [-i, i]:
            added_cheat, amount = get_cheat(grid, current_position, (x, y + dy), cutoff)
            tot_added_cheats += added_cheat
            if amount is not None:
                amounts[amount] += 1

    for i in range(1, size + 1):
        for dx in [-i, i]:
            added_cheat, amount = get_cheat(grid, current_position, (x + dx, y), cutoff)
            tot_added_cheats += added_cheat
            if amount is not None:
                amounts[amount] += 1
            for j in range(1, size + 1 - i):
                for dy in [j, -j]:
                    added_cheat, amount = get_cheat(
                        grid, current_position, (x + dx, y + dy), cutoff
                    )
                    tot_added_cheats += added_cheat
                    if amount is not None:
                        amounts[amount] += 1

    return tot_added_cheats, amounts


def get_cheat(
    grid: NDArray,
    current_position: Tuple[int, int],
    new_position: Tuple[int, int],
    cutoff: int = 100,
) -> int:
    """provide 1 if there is a cheat beyond the cutoff available at the new positon,
    otherwise 0"""
    new_x, new_y = new_position
    curr_x, curr_y = current_position

    l1_dist = abs(curr_x - new_x) + abs(curr_y - new_y)
    current_score = grid[current_position]

    if is_valid(new_x, new_y, grid) and not np.isinf(grid[new_x, new_y]):
        new_score = grid[new_x, new_y]

        # only improvements count as cheats
        score_diff = new_score - current_score
        if score_diff > 0 and score_diff - l1_dist >= cutoff:
            return 1, score_diff - l1_dist
    return 0, None


if __name__ == "__main__":
    solve2("data/day20/input")
