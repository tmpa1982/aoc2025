from day10.button import Button


class LightsState:
    def __init__(self, lights: list[bool]):
        self.lights = lights

    @staticmethod
    def parse(s: str) -> LightsState:
        lights = [c == "#" for c in s.strip("[]")]
        return LightsState(lights)

    def get_initial_state(self) -> LightsState:
        return LightsState([False] * len(self.lights))

    def switch(self, button: Button) -> LightsState:
        new_lights = self.lights[:]
        for pos in button.positions:
            new_lights[pos] = not new_lights[pos]
        return LightsState(new_lights)

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, LightsState):
            return False
        return self.lights == value.lights

    def __hash__(self) -> int:
        return hash(tuple(self.lights))

    def __repr__(self) -> str:
        lights_str = "".join("#" if light else "." for light in self.lights)
        return f"LightsState({lights_str})"
