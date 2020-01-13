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

    # To draw this box
    def draw(self, window):
        font = pg.font.Font("resources/OpenSans-Regular.ttf", 26)
        gap = self.width / 9

        # Calculate drawing position relative to this box in board
        x = self.col * gap
        y = self.row * gap

        if self.temp != 0 and self.value == 0:
            text = font.render(str(self.temp), 1, self.COLOR_GRAY)
            window.blit(text, (x + 3, y + 3))  # Draw small number in upper-left corner
        elif self.value != 0:
            text = font.render(str(self.value), 1, self.COLOR_BLACK)
            window.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))  # Draw number in the middle

        if self.selected:
            pg.draw.rect(window, self.COLOR_RED, (x, y, gap, gap), 3)  # If this box selected, draw red box

    def set(self, val):
        self.value = val

    def set_temp(self, val):
        self.temp = val
