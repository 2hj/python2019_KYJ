import pygame as pg

pg.init()

screen = pg.display.set_mode((500, 500))

pg.display.set_caption("testing")

x = 50
y = 425
width = 40
height = 60
vel = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

#mainLoop
run = True
while run:
    pg.time.delay(50)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT] and x > vel:
        x -= vel
    if keys[pg.K_RIGHT] and x < 500 - width - vel:
        x += vel
    if not (isJump):
        if keys[pg.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount = -1
        else:
            isJump = False
            jumpCount = 10

    screen.fill((0,0,0))
    pg.draw.rect(screen, (255, 0, 0), (x, y, width, height))
    pg.display.update()

pg.quit()
