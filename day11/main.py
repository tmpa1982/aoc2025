from day11.solution2 import solve2
from .graph import Graph


def main():
    with open("day11/input.txt") as f:
        input = [line.strip() for line in f.readlines()]

    graph = Graph.create(input)
    print("Statistics:", graph.stats())
    paths = graph.find_all_paths()
    print(f"Part 1: {len(paths)}")

    result = solve2(graph)
    print(f"Part 2: {result}")

if __name__ == "__main__":
    main()
