from day10.button import Button
from day10.lights_state import LightsState


class LightsMachine:
    def __init__(self, desired_state: LightsState, buttons: list[Button]):
        self.desired_state = desired_state
        self.buttons = buttons

    @staticmethod
    def parse(s: str) -> LightsMachine:
        parts = s.split(" ")
        desired_state = LightsMachine.parse_desired_state(parts[0])
        buttons = LightsMachine.parse_buttons(parts[1:-1])
        return LightsMachine(desired_state, buttons)

    @staticmethod
    def parse_desired_state(s: str) -> LightsState:
        return LightsState.parse(s)
    
    @staticmethod
    def parse_buttons(parts: list[str]) -> list[Button]:
        return [Button.parse(part) for part in parts]

    def find_shortest_path(self) -> list[Button]:
        visited_states: set[LightsState] = set()
        initial = self.desired_state.get_initial_state()
        queue: list[list[tuple[Button, LightsState]]] = [[(Button([]), initial)]]
        while queue:
            path = queue.pop(0)
            current = path[-1]
            current_state = current[1]
            if current_state in visited_states:
                continue
            visited_states.add(current_state)
            if current_state == self.desired_state:
                return [step[0] for step in path][1:]
            for button in self.buttons:
                switched = current_state.switch(button)
                new_path = path + [(button, switched)]
                queue.append(new_path)
        return []

    def __repr__(self) -> str:
        return f"LightsMachine(desired_state={self.desired_state}, buttons={self.buttons})"