import json

from board import Board

def load_board(index: int):
    with open(f"data/layout.json") as f:
        data = json.load(f)[index]

    board = Board()
    for i in range(9):
        for j in range(9):
            if data[str(i)][j]:
                board.set_board(i, j, data[str(i)][j])
    print(board)
    return board

def main(index: int):
    board = load_board(index)
    while board.unsolved > 33:
        print(board.unsolved)
        for i in range(1, 10):
            board.solve_number(i)
        board.solve_square()
        print(board)
    board.solve_number(1)
    print(board)

main(1)