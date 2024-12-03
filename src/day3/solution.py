"""solution for day three"""

from typing import List
import re


def load_data() -> List[str]:
    """load the data"""
    with open("data/day3/input", "r") as f:
        data = f.read().splitlines()
    return data


def solve1(data: List[str]):
    """solve the first half of the problem"""
    total_products = 0
    for string in data:
        matches = re.findall(r"mul\((\d+),(\d+)\)", string)
        for match in matches:
            x, y = map(int, match)
            total_products += x * y

    print(total_products)


def solve2():
    """solve the second half of the problem"""
    data = load_data()
    tot_str = "".join(data)
    new_data = []

    substrings = tot_str.split("don't()")
    new_data.append(substrings[0])
    substrings = substrings[1:]

    for substring in substrings:
        subsubstrings = substring.split("do()")
        for subsubstring in subsubstrings[1:]:
            new_data.append(subsubstring)

    solve1(new_data)


if __name__ == "__main__":
    # data = load_data()
    # solve1(data)
    solve2()
