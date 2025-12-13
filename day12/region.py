from day12 import shapes


class Region:
    def __init__(self, width: int, height: int, required_boxes: list[int]) -> None:
        self.width = width
        self.height = height
        self.required_boxes = required_boxes

    @staticmethod
    def parse(s: str) -> Region:
        parts = s.split(" ")
        [width, height] = parts[0].strip(":").split("x")
        required_boxes = [int(x) for x in parts[1:]]
        return Region(int(width), int(height), required_boxes)

    def is_trivial_fit(self) -> bool:
        x = self.width // 3
        y = self.height // 3
        total = x * y
        return sum(self.required_boxes) <= total

    def is_trivial_no_fit(self) -> bool:
        total_required = 0
        for index, amount in enumerate(self.required_boxes):
            shape = shapes.shapes[index]
            total_required += Region.__total(shape) * amount
        total_area = self.width * self.height
        return total_required > total_area

    @staticmethod
    def __total(shape: list[list[bool]]) -> int:
        total = 0
        for row in shape:
            for cell in row:
                if cell:
                    total += 1
        return total