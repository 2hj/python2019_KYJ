import pygame as pg

pg.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

imgs = pg.image.load("images/textbox.png").convert_alpha()

def mying(x,y):
    screen.blit(imgs(x,y))

x = (SCREEN_WIDTH * 0.5)
y = (SCREEN_HEIGHT * 0.5)

finished = False
while not finished:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
    screen.fill((255, 255, 255))
    mying(x,y)
    pg.display.flip()

pg.quit()
quit()
