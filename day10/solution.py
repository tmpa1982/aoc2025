from scipy.optimize import milp, LinearConstraint # type: ignore
import numpy as np

from day10.joltage import Joltage
from day10.lights_machine import LightsMachine


def solve(input: list[str]) -> int:
    result = 0
    for line in input:
        machine = LightsMachine.parse(line)
        path = machine.find_shortest_path()
        result += len(path)
    return result

def solve2(input: list[str]) -> int:
    result = 0
    for line in input:
        machine = LightsMachine.parse(line)
        buttons = np.array(machine.button_matrix())
        desired = np.array(machine.joltage.joltages)
        button_pushes = find_minimum_button_pushes(buttons, desired)
        verified_joltage = verify_button_pushes(machine, button_pushes)
        if verified_joltage != machine.joltage:
            print(f"Error with line: {line}")
            break
        result += sum(button_pushes)
    return result

def find_minimum_button_pushes(array: np.ndarray, desired: np.ndarray) -> list[int]:
    n = array.shape[0]
    result = milp(
        np.ones(n),
        constraints=LinearConstraint(array.T, desired, desired), # type: ignore
        integrality = np.ones(n),
    )
    return [round(x) for x in result.x] # type: ignore

def verify_button_pushes(machine: LightsMachine, button_pushes: list[int]) -> Joltage:
    joltage = machine.joltage.get_initial_state()
    for index, times in enumerate(button_pushes):
        joltage = joltage.switch(machine.buttons[index], times)
    return joltage
