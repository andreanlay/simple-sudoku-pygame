import pygame as pg
from Board import Board
from Box import Box
import util


class Game:
    def __init__(self, width, height):
        self.board = Board()
        self.row = self.col = 9
        self.boxes = [[Box(self.board.board[i][j], i, j, width, height) for j in range(9)] for i in range(9)]
        self.width = width
        self.height = height
        self.selected = None

    def place(self, val):
        row, col = self.selected
        self.boxes[row][col].set(val)

    def place_temp(self, val):
        row, col = self.selected
        self.boxes[row][col].set_temp(val)

    def draw(self, window):
        gap = self.width / 9
        for i in range(self.row + 1):
            if i % 3 == 0 and i != 0:  # Draw thicker border every 3x3 box
                thick = 4
            else:
                thick = 1
            pg.draw.line(window, (0, 0, 0), (0, i * gap), (self.width, i * gap), thick)  # Draw horizontal line
            pg.draw.line(window, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)  # Draw vertical line

        for i in range(9):
            for j in range(9):
                self.boxes[i][j].draw(window)

    def select(self, row, col):
        # Reset other box selected status
        for i in range(9):
            for j in range(9):
                self.boxes[i][j].selected = False
        row, col = int(row), int(col)
        self.boxes[row][col].selected = True  # Mark current clicked box as selected
        self.selected = (row, col)

    def clear(self):
        row, col = self.selected

        # Clear selected box attributes
        self.boxes[row][col].set(0)
        self.boxes[row][col].set_temp(0)

    def click(self, pos):
        if pos[0] < self.width and pos[1] < self.height:  # check if user clicked on valid position on board
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return (y, x)
        elif pos[0] <= 60 and pos[1] >= 540:  # If clicked on '?' icon, show help message
            help_str = "Press 1 - 9 to enter a number\n" \
                       "ENTER to place it on the board\n" \
                       "Press BACKSPACE to delete a number. Have fun!"
            util.show_messageBox("Help", help_str)
        else:
            return None

    def check_empty_box(self):
        for i in range(9):
            for j in range(9):
                if self.boxes[i][j] == 0:
                    return True
        return False

    def check_answer(self):
        self.board.solve()  # To solve current board
        for i in range(9):
            for j in range(9):
                if self.board.board[i][j] != self.boxes[i][j].value:
                    return False
        return True
