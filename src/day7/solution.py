"""solution for day 7"""

from equation import EquationValidator


def load_data():
    """load data"""
    with open("data/day7/input") as f:
        data = f.read().splitlines()

    results = []
    equations = []
    for item in data:
        left_side, right_side = item.split(":")
        results.append(int(left_side))
        equations.append(list(map(int, right_side.strip().split(" "))))

    return results, equations


def solve1():
    """solve part 1"""
    results, equation_parts = load_data()

    valid_targets_sum = 0
    for target, parts in zip(results, equation_parts):
        eqn = EquationValidator(parts)
        if eqn.is_valid(target):
            valid_targets_sum += target

    print(valid_targets_sum)


if __name__ == "__main__":
    solve1()
