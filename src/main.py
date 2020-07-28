import pygame as pg
import time
import util
from Game import Game


def redraw_window(win, board, time):
    win.fill((0, 0, 0))
    font = pg.font.Font("resources/OpenSans-Regular.ttf", 26)
    text = font.render("Time: " + util.format_time(time), 1, (255, 255, 255))
    win.blit(text, (540 - 160, 555))  # Draw time on bottom right corner

    text = font.render("?", 1, (255, 255, 255))
    win.blit(text, (20, 555))  # Draw help on bottom left corner

    board.draw(win)

def main():
    window = pg.display.set_mode((540, 600))
    pg.display.set_caption("Simple Sudoku")

    board = Game(540, 540)
    running = True
    pressed = None
    start = time.time()

    while running:
        current_time = round(time.time() - start)
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
            if e.type == pg.KEYDOWN:
                if util.get_key(e.key) is not None:
                    pressed = util.get_key(e.key)
                elif e.key == pg.K_BACKSPACE:
                    board.clear()
                    pressed = None
                elif e.key == pg.K_RETURN:
                    x, y = board.selected
                    board.place(pressed)
                    if board.check_empty_box() is False and board.check_answer() is True:  # If finished and correct
                        end_str = "You have completed this board in " + util.format_time(current_time) + \
                                  "\nPress OK to start a new game "
                        util.show_messageBox("Board completed!", end_str)
                        start = time.time()
                        board = Game(540, 540)
                        pressed = None

            if e.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    pressed = None
        if board.selected and pressed is not None:
            board.place_temp(pressed)

        redraw_window(window, board, current_time)
        pg.display.update()

pg.init()
main()
pg.quit()