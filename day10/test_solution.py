import numpy as np

from day10.lights_machine import LightsMachine
from day10.solution import solve, find_minimum_button_pushes


def test_solve_sample():
    input = [
        "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
        "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
        "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}",
    ]
    result = solve(input)
    
    assert result == 7

def test_find_minimum_button_pushes():
    machine = LightsMachine.parse("[...#...] (0,2,3,6) (0,1,4,6) (1,3,4,5) (1,2,4,6) (0,2,3,4,5) (2,3,6) (1,2) (2,3,4,5,6) {37,24,84,71,44,32,71}")
    buttons = np.array(machine.button_matrix())
    desired = np.array(machine.joltage.joltages)
    result = find_minimum_button_pushes(buttons, desired)
    joltage = machine.joltage.get_initial_state()
    for index, times in enumerate(result):
        joltage = joltage.switch(machine.buttons[index], times)
    assert joltage == machine.joltage
