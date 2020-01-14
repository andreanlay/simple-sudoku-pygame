import pygame as pg
from Board import Board
from Box import Box
from tkinter import *
from tkinter import messagebox

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