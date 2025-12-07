from tachyon import count_total_split

def main():
    with open("day7/input.txt", 'r') as file:
        input = file.readlines()
        result = count_total_split([s.strip("\n") for s in input])
        print(result)

if __name__ == "__main__":
    main()
