from paper_roll import Board

def main():
    with open("day4/input.txt", 'r') as file:
        input = file.readlines()
        board = Board([s.strip() for s in input])
        print(board.count_accessible())

if __name__ == "__main__":
    main()
