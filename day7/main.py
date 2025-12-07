from tachyon import count_total_paths, count_total_split

def main():
    with open("day7/input.txt", 'r') as file:
        input = file.readlines()
        cleaned = [s.strip("\n") for s in input]
        result = count_total_split(cleaned)
        print(f"Part 1: {result}")
        result = count_total_paths(cleaned)
        print(f"Part 2: {result}")

if __name__ == "__main__":
    main()
