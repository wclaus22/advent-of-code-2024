"""solution for day 14"""

import re
import numpy as np
from robot import Robot, get_safety, render_grid

import matplotlib.pyplot as plt


def load_data():
    """load the data"""
    with open("data/day14/input") as f:
        data = f.read().splitlines()

    positions = []
    velocities = []
    for line in data:
        res = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)

        positions.append((int(res.group(1)), int(res.group(2))))
        velocities.append((int(res.group(3)), int(res.group(4))))

    return positions, velocities


def solve1(seconds: int, x_size: int, y_size: int):
    """solve first part"""
    pos, vel = load_data()

    robots = []
    for p, v in zip(pos, vel):
        robot = Robot(p[0], p[1], v[0], v[1])
        robot.move(
            seconds,
            x_size,
            y_size,
        )
        robots.append(robot)
    safety = get_safety(robots, x_size, y_size)
    print(safety)


def solve2(max_seconds: int, x_size: int, y_size: int):
    """solve second part"""
    pos, vel = load_data()

    robots = []
    for p, v in zip(pos, vel):
        robot = Robot(p[0], p[1], v[0], v[1])
        robots.append(robot)

    for i in range(max_seconds):
        for robot in robots:
            robot.move(
                1,
                x_size,
                y_size,
            )
        grid = render_grid(robots, x_size, y_size)
        if np.mean(grid[38:69, 23:59]) > 0.1:
            plt.imshow(grid, cmap="gray")
            plt.savefig(f"data/day14/frames/frame_{i}.png")
            plt.close()


if __name__ == "__main__":
    solve2(10000, 101, 103)
