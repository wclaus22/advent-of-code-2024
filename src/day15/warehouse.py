"""warehouse & robot module"""

from typing import Tuple, Literal
import numpy as np


def get_init(grid: np.ndarray) -> Tuple[int, int]:
    """get the initial point idx in the grid"""
    x, y = np.where(grid == "@")
    return x[0], y[0]


class Robot:
    """robot for the warehouse"""

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, direction: Literal["^", "v", "<", ">"]) -> None:
        """move robot in the given direction"""
        if direction == "^":
            self.x -= 1
        elif direction == "v":
            self.x += 1
        elif direction == "<":
            self.y -= 1
        elif direction == ">":
            self.y += 1


class Warehouse:
    """warehouse to monitor the movements of the packages"""

    def __init__(self, grid: np.ndarray):
        self.grid = grid
        self.robot = Robot(*get_init(grid))

    def move_robot(self, direction: str) -> None:
        """move the robot in the given direction"""

        # first check for packages in the direction of movement
        if direction == "^":
            grid_slice = self.grid[: self.robot.x, self.robot.y][::-1]
            if _can_move(grid_slice):
                updated_slice = _push_packages(grid_slice)
                self.grid[: self.robot.x, self.robot.y] = updated_slice[::-1]

                self.grid[self.robot.x, self.robot.y] = "."
                self.robot.move(direction)

        elif direction == "v":
            grid_slice = self.grid[self.robot.x + 1 :, self.robot.y]
            if _can_move(grid_slice):
                updated_slice = _push_packages(grid_slice)
                self.grid[self.robot.x + 1 :, self.robot.y] = updated_slice

                self.grid[self.robot.x, self.robot.y] = "."
                self.robot.move(direction)

        elif direction == "<":
            grid_slice = self.grid[self.robot.x, : self.robot.y][::-1]
            if _can_move(grid_slice):
                updated_slice = _push_packages(grid_slice)
                self.grid[self.robot.x, : self.robot.y] = updated_slice[::-1]

                self.grid[self.robot.x, self.robot.y] = "."
                self.robot.move(direction)

        elif direction == ">":
            grid_slice = self.grid[self.robot.x, self.robot.y + 1 :]
            if _can_move(grid_slice):
                updated_slice = _push_packages(grid_slice)
                self.grid[self.robot.x, self.robot.y + 1 :] = updated_slice

                self.grid[self.robot.x, self.robot.y] = "."
                self.robot.move(direction)


def _push_packages(grid_slice: np.ndarray) -> np.ndarray:
    """push the packages in the given slice"""
    end_idx = grid_slice.tolist().index("#")
    start_slice = grid_slice[:end_idx].tolist()

    assert "." in start_slice, "There should be a free slot in the slice"
    start_idx = start_slice.index(".")

    for i in range(start_idx):
        grid_slice[i + 1] = grid_slice[i]
    grid_slice[0] = "@"

    return grid_slice


def _can_move(grid_slice: np.ndarray) -> bool:
    """check if the robot can move in the given direction"""
    return (
        "." in "".join(grid_slice).split("#", maxsplit=1)[0]
    )  # if there is a free slot, the robot can move


def get_gps(grid: np.ndarray) -> int:
    """get the sum of all GPS coordinates of the boxes"""
    x_idx, y_idx = np.where(grid == "O")

    final_sum = 0
    for x, y in zip(x_idx, y_idx):
        final_sum += x * 100 + y
    return final_sum
