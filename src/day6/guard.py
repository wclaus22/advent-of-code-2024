"""guard class to solve the problem of predicting where the guard will leave"""

from typing import Tuple, Literal


class Guard:
    """guard object to hold the guard's position and direction of movement"""

    def __init__(
        self,
        initial_position: Tuple[int, int],
        initial_direction: Literal["up", "down", "left", "right"] = "up",
    ):
        self.position = initial_position
        self.direction = initial_direction

    def move(
        self,
    ) -> None:
        """move the guard by one step in the current direction"""
        if self.direction == "up":
            self.position = (self.position[0] - 1, self.position[1])
        elif self.direction == "down":
            self.position = (self.position[0] + 1, self.position[1])
        elif self.direction == "left":
            self.position = (self.position[0], self.position[1] - 1)
        elif self.direction == "right":
            self.position = (self.position[0], self.position[1] + 1)

    def rotate(self) -> None:
        """rotate the guard by 90 degrees to the right"""
        if self.direction == "up":
            self.direction = "right"
        elif self.direction == "right":
            self.direction = "down"
        elif self.direction == "down":
            self.direction = "left"
        elif self.direction == "left":
            self.direction = "up"

    def look_ahead(self) -> Tuple[int, int]:
        """look ahead to see if the guard will hit a wall"""
        if self.direction == "up":
            return self.position[0] - 1, self.position[1]
        elif self.direction == "down":
            return self.position[0] + 1, self.position[1]
        elif self.direction == "left":
            return self.position[0], self.position[1] - 1
        elif self.direction == "right":
            return self.position[0], self.position[1] + 1
