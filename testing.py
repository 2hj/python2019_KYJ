import pygame as pg
import sys

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pg.init()
pg.display.set_caption("Simple Pygame Example")
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pos_x = 200
pos_y = 200

clock = pg.time.Clock()
while True:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    key_event = pg.key.get_pressed()
    if key_event[pg.K_LEFT]:
        pos_x -= 1
    if key_event[pg.K_RIGHT]:
        pos_x += 1
    if key_event[pg.K_UP]:
        pos_y -= 1
    if key_event[pg.K_DOWN]:
        pos_y += 1

    screen.fill(WHITE)
    pg.draw.circle(screen, BLACK, (pos_x, pos_y), 20)
    pg.display.update()
