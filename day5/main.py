from fresh_range import solve2

def main():
    with open("day5/input.txt", 'r') as file:
        input = file.readlines()
        result = solve2([s.strip() for s in input])
        print(result)

if __name__ == "__main__":
    main()
