from day10.button import Button


class Joltage:
    def __init__(self, joltages: list[int]):
        self.joltages = joltages

    @staticmethod
    def parse(s: str) -> Joltage:
        joltages = [int(c) for c in s.strip("{}").split(",")]
        return Joltage(joltages)

    def get_initial_state(self) -> Joltage:
        return Joltage([0] * len(self.joltages))

    def switch(self, button: Button, times: int) -> Joltage:
        new_joltages = self.joltages[:]
        for pos in button.positions:
            new_joltages[pos] = new_joltages[pos] + times
        return Joltage(new_joltages)

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Joltage):
            return False
        return self.joltages == value.joltages

    def __hash__(self) -> int:
        return hash(tuple(self.joltages))

    def __repr__(self) -> str:
        joltage_str = ",".join(str(joltage) for joltage in self.joltages)
        return f"Joltage({joltage_str})"
