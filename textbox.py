import testing2 as t2

imgs = pygame.image.load("./iamges/textbox.png")

def mying(x,y):
    screen.blit(imgs(x,y))

x = (SCREEN_WIDTH * 0.5)
y = (SCREEN_HEIGHT * 0.5)

finished = False

while not finished:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
    screen.fill(255, 255, 255)
    mying(x,y)
    pg.display.flip()
pg.quit()
quit()
