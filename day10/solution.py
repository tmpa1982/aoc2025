from scipy.optimize import milp, LinearConstraint # type: ignore
import numpy as np

from day10.lights_machine import LightsMachine


def solve(input: list[str]) -> int:
    result = 0
    for line in input:
        machine = LightsMachine.parse(line)
        path = machine.find_shortest_path()
        result += len(path)
    return result

def solve2(input: list[str]) -> int:
    for line in input:
        machine = LightsMachine.parse(line)
        num_buttons = len(machine.buttons)
        num_joltage = len(machine.joltage.joltages)
        if num_buttons > num_joltage:
            print(f"Warning: more buttons ({num_buttons}) than joltage ratings ({num_joltage})")
    return 0

def find_minimum_button_pushes(array: np.ndarray, desired: np.ndarray) -> list[int]:
    n = array.shape[0]
    result = milp(
        np.ones(n),
        constraints=LinearConstraint(array.T, desired, desired), # type: ignore
        integrality = np.ones(n),
    )
    return [int(x) for x in result.x] # type: ignore
