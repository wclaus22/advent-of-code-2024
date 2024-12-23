"""solution for day17"""

from typing import List, Tuple
from computer import Computer


def load_data(path: str) -> Tuple[List[int], List[int]]:
    """load the data and prepare registers and the program"""
    with open(path) as f:
        data = f.read().splitlines()
    split_idx = data.index("")
    program = data[split_idx + 1].split(":")[-1].strip().split(",")
    program = list(map(int, program))
    registers = [int(item.split(":")[-1].strip()) for item in data[:split_idx]]

    return registers, program


def run_program(computer: Computer, program: List[int]) -> None:
    """run the computer program"""

    while computer.instruction_pointer < len(program):
        opcode = program[computer.instruction_pointer]
        operand = program[computer.instruction_pointer + 1]
        computer.operation(opcode)(operand)


def solve1(path):
    """solve first part"""
    registers, program = load_data(path)
    computer = Computer(*registers)
    run_program(computer, program)
    print(",".join(map(str, computer.outputs)))


def solve2(path, min_register=0, max_register=200000):
    """try to solve it brute force hehehe"""
    registers, program = load_data(path)
    _, b, c = registers
    for a in range(min_register, max_register):
        if a % 100000 == 0:
            print(
                round((a - min_register) / (max_register - min_register) * 100, 3), "%"
            )
        computer = Computer(a, b, c)
        run_program(computer, program)
        if computer.outputs == program:
            print("Completed with register value A:", a)
            break
    else:
        print("No register found between", min_register, max_register)


if __name__ == "__main__":
    solve2("data/day17/input", min_register=5000000, max_register=100000000)
