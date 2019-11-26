from pygame_functions import *

screenSize(1280, 960)
setBackgroundColour("dark green")

idle = makeSprite("idle/idle1.png")
addSpriteImage(idle, "idle/idle2.png")
addSpriteImage(idle, "idle/idle3.png")
addSpriteImage(idle, "idle/idle4.png")
addSpriteImage(idle, "idle/idle5.png")
addSpriteImage(idle, "idle/idle6.png")
addSpriteImage(idle, "idle/idle7.png")
addSpriteImage(idle, "idle/idle8.png")
addSpriteImage(idle, "idle/idle9.png")
addSpriteImage(idle, "idle/idle10.png")
addSpriteImage(idle, "idle/idle11.png")
addSpriteImage(idle, "idle/idle12.png")
addSpriteImage(idle, "idle/idle13.png")
addSpriteImage(idle, "idle/idle14.png")
addSpriteImage(idle, "idle/idle15.png")
addSpriteImage(idle, "idle/idle16.png")

idleX = 200
idleImage = 0

moveSprite(idle, 300, 100, True)
showSprite(idle)

nextFrame = clock()
print("nextFrame:", nextFrame)

frame = 0

while True:
    if keyPressed("right"):
        print("clock():", clock())
        if clock() > nextFrame:
            idleImage += 1
            if idleImage > 7:
                idleImage = 0
            changeSpriteImage(idle, idleImage)
            nextFrame = clock() + 60

        # idleX += 7
        if idleX > 1024:
            idleX = -20

        moveSprite(idle, idleX, 120)
