from random import randint

class Board:
    def __init__(self):
        self.board = [[0] * 9 for _ in range(9)]
        self.generate_board()

    def generate_board(self):
        self.fill_all_boxes()
        self.remove_elements(32)

    def fill_all_boxes(self):
        flag = [False for _ in range(9)]
        empty = self.find_empty()
        
        #If no empty box, finish generating
        if empty is None:
            return True

        row, col = empty[0], empty[1]
        while True:
            num = randint(1, 9)
            flag[num - 1] = True
            if self.safe_to_fill(row, col, num):
                self.board[row][col] = num
                if self.fill_all_boxes():
                    return True
                self.board[row][col] = 0
                
            # If none of numbers fit, backtrack to previous block
            if flag.count(True) == 9:
                return False
    
    def remove_elements(self, count):
        while count != 0:
            index = randint(0, 80)
            row, col = int(index / 9), index % 9
            while self.board[row][col - 1 if col != 0 else col] == 0:
                index = randint(0, 80)
                row, col = int(index / 9), index % 9 - 1
            self.board[row][col - 1 if col != 0 else col] = 0
            count -= 1

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
