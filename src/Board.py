from random import randint


class Board:
    def __init__(self):
        self.board = [[0] * 9 for _ in range(9)]
        self.generate_board()

    def generate_board(self):
        self.fill_diagonal_boxes()
        self.fill_remaining_boxes()

    def fill_diagonal_boxes(self):
        for i in range(0, 9, 3):
            for k in range(3):
                for l in range(3):
                    num = randint(1, 9)
                    while self.innerbox_is_safe(i, i, num) is False:
                        num = randint(1, 9)
                    self.board[i+k][i+l] = num

    def fill_remaining_boxes(self):
        flag = [False for _ in range(9)]
        empty = self.find_empty()

        # If no empty box, finish generating
        if empty is None:
            return True

        row, col = empty[0], empty[1]
        while True:
            num = randint(1, 9)
            flag[num - 1] = True
            if self.safe_to_fill(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining_boxes():
                    return True
                self.board[row][col] = 0

            # If none of numbers fit, backtrack to previous block
            if flag.count(True) == 9:
                return False

    # Check entire row whether a number is used
    def row_is_safe(self, row, num):
        for i in range(9):
            if self.board[row][i] == num:
                return False
        return True

    # Check entire column whether a number is used
    def col_is_safe(self, col, num):
        for i in range(9):
            if self.board[i][col] == num:
                return False
        return True

    # Check 3x3 box whether a number is used
    def innerbox_is_safe(self, row, col, num):
        for i in range(3):
            for j in range(3):
                if self.board[row + i][col + j] == num:
                    return False
        return True

    def safe_to_fill(self, row, col, num):
        return self.row_is_safe(row, num) and self.col_is_safe(col, num) and self.innerbox_is_safe(row - row % 3,
                                                                                                   col - col % 3,
                                                                                                   num)

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return [i, j]
        return None
