class Button:
    def __init__(self, positions: list[int]):
        self.positions = positions

    @staticmethod
    def parse(s: str) -> Button:
        positions = [int(n) for n in s.strip("()").split(",")]
        return Button(positions)

    def __repr__(self) -> str:
        return f"Button({self.positions})"
    
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Button):
            return False
        return self.positions == value.positions
