"""computer module"""

from typing import Callable


class Computer:
    """class holding register and operations"""

    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c
        self.instruction_pointer = 0
        self.outputs = []

    def operation(self, opcode: int) -> Callable:
        """apply the correct operation to the given inputs"""
        _func_map = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }
        return _func_map[opcode]

    def adv(self, operand: int) -> None:
        """division operation"""
        self.a = self.a // (2 ** self.combo_operand(operand))
        self.instruction_pointer += 2

    def bxl(self, operand: int) -> None:
        """bitwise XOR"""
        self.b = self.b ^ operand
        self.instruction_pointer += 2

    def bst(self, operand: int) -> None:
        """modulo 8"""
        self.b = self.combo_operand(operand) % 8
        self.instruction_pointer += 2

    def jnz(self, operand: int) -> None:
        """do nothing if A register is 0"""
        if self.a != 0:
            self.instruction_pointer = operand
        else:
            self.instruction_pointer += 2

    def bxc(self, operand: int) -> None:
        """bitwise XOR of registers B and C"""
        self.b = self.b ^ self.c
        self.instruction_pointer += 2

    def out(self, operand: int) -> None:
        """combo operand modulo 8 and add to outputs"""
        self.outputs.append(self.combo_operand(operand) % 8)
        self.instruction_pointer += 2

    def bdv(self, operand: int) -> None:
        """adv instruction but stored in the B register"""
        self.b = self.a // (2 ** self.combo_operand(operand))
        self.instruction_pointer += 2

    def cdv(self, operand: int) -> None:
        """adv instruction but stored in the C register"""
        self.c = self.a // (2 ** self.combo_operand(operand))
        self.instruction_pointer += 2

    def combo_operand(self, operand: int):
        """unravel the combo operand"""

        # literal operand
        if 0 <= operand <= 3:
            return operand
        if operand == 4:
            return self.a
        if operand == 5:
            return self.b
        if operand == 6:
            return self.c
        raise ValueError("Invalid operand found.")
