from .graph import Graph


def main():
    with open("day11/input.txt") as f:
        input = [line.strip() for line in f.readlines()]

    graph = Graph.create(input)
    paths = graph.find_all_paths()
    print(f"Part 1: {len(paths)}")

if __name__ == "__main__":
    main()
