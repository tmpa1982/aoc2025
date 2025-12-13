from day10.button import Button
from day10.lights_state import LightsState


def test_switch():
    state = LightsState([False, False, True, False, False])
    button = Button([1, 2, 3])
    result = state.switch(button)
    assert result == LightsState([False, True, False, True, False])
    assert state == LightsState([False, False, True, False, False])
