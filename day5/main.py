from fresh_range import solve

def main():
    with open("day5/input.txt", 'r') as file:
        input = file.readlines()
        result = solve([s.strip() for s in input])
        print(result)

if __name__ == "__main__":
    main()
