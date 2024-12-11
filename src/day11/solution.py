"""solution for day 11"""

from collections import defaultdict


def load_data():
    """load the data"""
    with open("data/day11/input") as f:
        data = f.read().splitlines()[0]
    return list(map(int, data.split(" ")))


def solve1(n_blinks: int):
    """solve first part (brute force)"""
    numbers = load_data()
    for _ in range(n_blinks):
        numbers_new = []
        for number in numbers:

            # apply rules
            if number == 0:
                numbers_new.append(1)
            elif (len_number := len(str(number))) % 2 == 0:
                left, right = (
                    int(str(number)[: len_number // 2]),
                    int(str(number)[len_number // 2 :]),
                )
                numbers_new.append(left)
                numbers_new.append(right)
            else:
                numbers_new.append(number * 2024)
        numbers = numbers_new
    print(len(numbers))


def solve2(n_blinks: int):
    """solve the second part (aka solve the first part a different way)"""
    numbers = load_data()
    numbers_cnt = defaultdict(int)
    for number in numbers:
        numbers_cnt[number] += 1
    for _ in range(n_blinks):
        new_numbers_cnt = defaultdict(int)
        for number, cnt in numbers_cnt.items():
            # apply rules
            if number == 0:
                new_numbers_cnt[1] += cnt
            elif (len_number := len(str(number))) % 2 == 0:
                left, right = (
                    int(str(number)[: len_number // 2]),
                    int(str(number)[len_number // 2 :]),
                )
                new_numbers_cnt[left] += cnt
                new_numbers_cnt[right] += cnt
            else:
                new_numbers_cnt[number * 2024] += cnt
        numbers_cnt = new_numbers_cnt

    tot_numbers = 0
    for _, cnt in numbers_cnt.items():
        tot_numbers += cnt

    print(tot_numbers)


if __name__ == "__main__":
    solve2(75)
