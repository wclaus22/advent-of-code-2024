"""solution for day5"""

import numpy as np


def load_data():
    """load data from file"""
    with open("data/day5/input") as f:
        data = f.read().splitlines()

    split_idx = data.index("")
    rules = data[:split_idx]
    updates = [item.split(",") for item in data[split_idx + 1 :]]

    return rules, updates


def is_valid(rules, update):
    """brute force check if the update is valid w.r.t. the rules"""
    for rule in rules:
        first_value, second_value = rule.split("|")

        if first_value not in update or second_value not in update:
            continue

        first_index = update.index(first_value)
        second_index = update.index(second_value)

        if second_index < first_index:
            return False

    return True


def solve1():
    """solve the first part"""
    rules, updates = load_data()
    all_center_values = 0
    for update in updates:
        center_value = update[len(update) // 2]

        if is_valid(rules, update):
            all_center_values += int(center_value)

    print(all_center_values)


def reorder(rules, update):
    """reorder the items in the update based on the rules"""
    for rule in rules:
        first_value, second_value = rule.split("|")

        if first_value not in update or second_value not in update:
            continue

        first_index = update.index(first_value)
        second_index = update.index(second_value)

        if second_index < first_index:
            del update[second_index]
            update.insert(first_index, second_value)


def solve2():
    """solve the second part"""
    rules, updates = load_data()
    all_center_values = 0
    for update in updates:

        if not is_valid(rules, update):
            while not is_valid(rules, update):
                reorder(rules, update)
            center_value = update[len(update) // 2]
            all_center_values += int(center_value)

    print(all_center_values)


if __name__ == "__main__":
    solve2()
