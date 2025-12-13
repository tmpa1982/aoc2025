from day10.button import Button
from day10.lights_machine import LightsMachine
from day10.lights_state import LightsState


def test_path_trivial():
    desired_state = LightsState([False, True, True, True, False])
    button = Button([1, 2, 3])
    machine = LightsMachine(desired_state, [button], [])
    result = machine.find_shortest_path()
    assert result == [button]

def test_path_one_step_other_button():
    desired_state = LightsState([False, True, True, True, False])
    button1 = Button([0, 1, 2])
    button2 = Button([1, 2, 3])
    machine = LightsMachine(desired_state, [button1, button2], [])
    result = machine.find_shortest_path()
    assert result == [button2]

def test_path_two_steps():
    machine = LightsMachine.parse("[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}")
    print(machine)
    result = machine.find_shortest_path()
    expected_buttons1 = [Button([0, 2]), Button([0, 1])]
    expected_buttons2 = [Button([1, 3]), Button([2, 3])]
    assert result == expected_buttons1 or result == expected_buttons2
