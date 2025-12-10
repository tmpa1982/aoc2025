from coordinate_2d import Coordinate2D


class Board:
    cells: list[list[bool]]

    def __init__(self, max_x: int, max_y: int):
        self.max_x = max_x
        self.max_y = max_y
        self.cells = [[False for _ in range(max_x+1)] for _ in range(max_y+1)]

    def is_marked(self, x: int, y: int):
        return self.cells[y][x]

    def mark_cell(self, x: int, y: int):
        if x > self.max_x:
            raise ValueError(f"x too large: {x} > {self.max_x}")
        if y > self.max_y:
            raise ValueError(f"y too large: {y} > {self.max_y}")

        self.cells[y][x] = True

    def mark_line(self, c1: Coordinate2D, c2: Coordinate2D):
        if c1.x == c2.x:
            self.mark_vertical(c1.y, c2.y, c1.x)
        elif c1.y == c2.y:
            self.mark_horizontal(c1.x, c2.x, c1.y)
        else:
            raise ValueError(f"Invalid line: {c1} {c2}")

    def mark_vertical(self, y1: int, y2: int, x: int):
        min_y = min(y1, y2)
        max_y = max(y1, y2)
        
        for y in range(min_y, max_y + 1):
            self.mark_cell(x, y)

    def mark_horizontal(self, x1: int, x2: int, y: int):
        min_x = min(x1, x2)
        max_x = max(x1, x2)
        
        for x in range(min_x, max_x + 1):
            self.mark_cell(x, y)

    def fill_closed_area(self):
        (x, y) = self.find_first_corner()
        self.fill_area(x+1, y+1)

    def find_first_corner(self) -> tuple[int, int]:
        for y in range(len(self.cells)):
            row = self.cells[y]
            for x in range(len(row)):
                if row[x]:
                    return (x, y)
        return NotImplemented

    def fill_area(self, start_x: int, start_y: int):
        if self.cells[start_y][start_x]:
            raise ValueError(f"Cell is filled at {start_x} {start_y}")
        
        stack: list[tuple[int, int]] = [(start_x, start_y)]
        while len(stack) > 0:
            (x, y) = stack.pop()
            self.cells[y][x] = True
                
            if not self.cells[y-1][x]:
                self.cells[y-1][x] = True
                stack.append((x, y-1))
            if not self.cells[y+1][x]:
                self.cells[y+1][x] = True
                stack.append((x, y+1))
            if not self.cells[y][x-1]:
                self.cells[y][x-1] = True
                stack.append((x-1, y))
            if not self.cells[y][x+1]:
                self.cells[y][x+1] = True
                stack.append((x+1, y))

    def fill_row(self, row: list[bool]):
        indices: list[int] = self.find_true_indices(row)
        if len(indices) % 2 != 0:
            raise ValueError(f"Row has odd number of boundary cells: {len(indices)}")

        for i in range(len(indices)//2):
            from_index = indices[i]
            to_index = indices[i+1]
            for idx in range(from_index, to_index):
                row[idx] = True

    def find_true_indices(self, row: list[bool]) -> list[int]:
        result: list[int] = []
        for i in range(len(row)):
            if row[i]:
                result.append(i)
        return result

    def __repr__(self) -> str:
        rows = [self.repr_row(row) for row in self.cells]
        return "\n".join(rows)

    def repr_row(self, row: list[bool]) -> str:
        return "".join(["1" if c else "0" for c in row])
