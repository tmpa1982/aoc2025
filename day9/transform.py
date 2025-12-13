from day9.coordinate_2d import Coordinate2D


def main():
    with open("day9/input.txt", 'r') as file:
        input = file.readlines()
        cleaned = [s.strip("\n") for s in input]
        parsed = [Coordinate2D.create(c) for c in cleaned]
        (min_x, min_y) = get_minimums(parsed)
        with open("day9/input_transformed.txt", "w") as f:
            for c in parsed:
                f.write(f"{c.x - min_x},{c.y - min_y}\n")

def get_minimums(coordinates: list[Coordinate2D]) -> tuple[int, int]:
        min_x = coordinates[0].x
        min_y = coordinates[0].y
        for c in coordinates[1:]:
            if c.x < min_x:
                min_x = c.x
            if c.y < min_y:
                min_y = c.y
        return (min_x, min_y)

if __name__ == "__main__":
    main()
