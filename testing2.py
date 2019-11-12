import pygame as pg
import sys

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pg.init()
pg.display.set_caption("Simple Pygame Example")
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

textbox = pg.image.load("images/textbox.png")

position = (0, 0)

clock = pg.time.Clock()
print(clock)
while True:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            position = pg.mouse.get_pos()
        if event.type == pg.QUIT:
            sys.exit()

    # position = pg.mouse.get_pos()

    screen.fill(WHITE)
    screen.blit(textbox, (100, 100))
    pg.draw.circle(screen, BLACK, position, 20)
    pg.display.update()
