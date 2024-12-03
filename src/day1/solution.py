"""solution for day one"""

from typing import List, Tuple


def load_data() -> Tuple[List[int], List[int]]:
    """load the data"""
    with open("data/day1/input", "r") as f:
        data = f.read().splitlines()
    array1 = []
    array2 = []
    for item in data:
        array1.append(int(item.split(" ")[0]))
        array2.append(int(item.split(" ")[-1]))
    return array1, array2


def solve1():
    """solve the problem"""
    array1, array2 = load_data()
    diff = 0
    for item1, item2 in zip(sorted(array1), sorted(array2)):
        diff += abs(item1 - item2)

    print(diff)


def solve2():
    """solve the problem"""
    array1, array2 = load_data()
    array2_count = {}
    for item in array2:
        cnt = array2_count.get(item, 0)
        cnt += 1
        array2_count[item] = cnt

    similarity = 0
    for item in array1:
        cnt = array2_count.get(item, 0)
        similarity += cnt * item

    print(similarity)


if __name__ == "__main__":
    solve2()
