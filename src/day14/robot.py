"""robots module"""

from typing import List
import numpy as np


class Robot:
    """
    class to encapsulate robot behavior
    """

    def __init__(self, x: int, y: int, v_x: int, v_y: int):
        """
        Parameters
        ----------
        x : int
            x coordinate of robot
        y : int
            y coordinate of robot
        v_x : int
            x velocity of robot
        v_y : int
            y velocity of robot

        Returns
        -------
        NoneType
            None
        """
        self.x = x
        self.y = y

        self.v_x = v_x
        self.v_y = v_y

    def move(self, seconds: int, x_size: int, y_size: int) -> None:
        """move robot in given direction by distance"""

        self.x = (self.x + self.v_x * seconds) % x_size
        self.y = (self.y + self.v_y * seconds) % y_size

    def __repr__(self):
        return f"({self.x}, {self.y})"


def get_safety(robots: List[Robot], x_size: int, y_size: int) -> int:
    """get safety of robots"""

    quadrants = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
    }
    for robot in robots:
        if robot.x < x_size // 2 and robot.y < y_size // 2:
            quadrants[1] += 1
        elif robot.x > x_size // 2 and robot.y < y_size // 2:
            quadrants[2] += 1
        elif robot.x < x_size // 2 and robot.y > y_size // 2:
            quadrants[3] += 1
        elif robot.x > x_size // 2 and robot.y > y_size // 2:
            quadrants[4] += 1
    return quadrants[1] * quadrants[2] * quadrants[3] * quadrants[4]


def render_grid(robots: List[Robot], x_size: int, y_size: int) -> str:
    """render grid"""

    grid = np.zeros((x_size, y_size))
    for robot in robots:
        grid[robot.x][robot.y] = 1
    return grid
