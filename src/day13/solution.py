"""solution for day13"""

from matrix import format_input, solve_problem


def load_data():
    """load the data"""
    with open("data/day13/input") as f:
        data = f.read().splitlines()

    sublists = []
    sublist = []
    for line in data:
        if line == "":
            sublists.append(sublist)
            sublist = []
        else:
            sublist.append(line)
    sublists.append(sublist)

    return sublists


def solve1():
    """solve first part"""
    data = load_data()
    problems, solutions = format_input(data, 10000000000000)

    total_tokens = 0
    for problem, solution in zip(problems, solutions):
        solved_parameters = solve_problem(problem, solution)
        a, b = solved_parameters
        print(a, b)

        # is valid solution if both a and b are integers
        if round(a, 2).is_integer() and round(b, 2).is_integer():
            total_tokens += a * 3 + b  # 3 tokens for A, 1 token for B

    print(total_tokens)


if __name__ == "__main__":
    solve1()
