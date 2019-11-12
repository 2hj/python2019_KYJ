import pygame as pg
from pygame.locals import *

pg.init()
SCREEN_WIDTH,SCREEN_HEIGHT = 930, 480
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

imgs = pg.image.load('images/textbox.png')
# imgs_fixed = pg.transform.scale(imgs, (340, 100))

while 1:
    screen.fill((255, 255, 255))
    screen.blit(imgs, (120, 270))
    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit(0)
