from number import Number

class Board:
    def __init__(self):
        self.board = [[Number() for _ in range(9)] for _ in range(9)]
        self.unsolved = 81

    def set_board(self, x: int, y: int, num: int):
        self.board[x][y].set_value(num)
        self.unsolved -= 1
    
    def solve_square(self):
        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                values = set(range(1, 10))
                for i in range(3):
                    for j in range(3):
                        num = self.board[row_start + i][col_start + j].num
                        if num:
                            values.discard(num)
                if len(values) == 1:
                    missing_value = values.pop()
                    for i in range(3):
                        for j in range(3):
                            if self.board[row_start + i][col_start + j].num is None:
                                self.board[row_start + i][col_start + j].set_value(missing_value)
                                self.unsolved -= 1
    
    def solve_number(self, num: int):
        row_location = []
        col_location = []
        for row_idx in range(9):
            for col_idx in range(9):
                if self.board[row_idx][col_idx].num == num:
                    row_location.append(row_idx)
                    col_location.append(col_idx)
        
        for row_idx in range(9):
            for col_idx in range(9):
                if row_idx in row_location or col_idx in col_location:
                    self.board[row_idx][col_idx].remove_probability(num)

        for row_idx in range(9):
            for col_idx in range(9):
                if len(self.board[row_idx][col_idx].probability) == 1:
                    self.board[row_idx][col_idx].set_value(self.board[row_idx][col_idx].probability[0])
                    self.unsolved -= 1

    def __repr__(self):
        board_string = []
        for row in self.board:
            line_string = [str(cell) if cell.num is not None else "." for cell in row]
            board_string.append(" ".join(line_string))

        return "\n  SUDOKU BOARD\n\n" + "\n".join(board_string) + "\n"