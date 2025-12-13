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
