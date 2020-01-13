import pygame as pg


class Box:
    row = 9
    col = 9
    COLOR_GRAY = (128, 128, 128)
    COLOR_BLACK = (0, 0, 0)
    COLOR_RED = (255, 0, 0)

    def __init__(self, val, row, col, width, height):
        self.value = val  # Current box value
        self.temp = 0  # To indices this box potential fitting number
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False  # To mark whether this box is selected