from pygame_functions import *

screenSize(1280, 900)
setBackgroundColour("dark green")

class stopedCharacter:

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

    idleImage = 0

    # moveSprite(idle, 680, 450, True)
    # showSprite(idle)

    # nextFrame = clock()
    # print("nextFrame:", nextFrame)

    # frame = 0

class walkCharacter:

    walk = makeSprite("walk/Walk1.png")
    addSpriteImage(walk, "walk/Walk2.png")
    addSpriteImage(walk, "walk/Walk3.png")
    addSpriteImage(walk, "walk/Walk4.png")
    addSpriteImage(walk, "walk/Walk5.png")
    addSpriteImage(walk, "walk/Walk6.png")
    addSpriteImage(walk, "walk/Walk7.png")
    addSpriteImage(walk, "walk/Walk8.png")
    addSpriteImage(walk, "walk/Walk9.png")
    addSpriteImage(walk, "walk/Walk10.png")
    addSpriteImage(walk, "walk/Walk11.png")
    addSpriteImage(walk, "walk/Walk12.png")
    addSpriteImage(walk, "walk/Walk13.png")
    addSpriteImage(walk, "walk/Walk14.png")
    addSpriteImage(walk, "walk/Walk15.png")
    addSpriteImage(walk, "walk/Walk16.png")
    addSpriteImage(walk, "walk/Walk17.png")
    addSpriteImage(walk, "walk/Walk18.png")
    addSpriteImage(walk, "walk/Walk19.png")
    addSpriteImage(walk, "walk/Walk20.png")

    walkX = 200
    walkImage = 0

    # moveSprite(walk, 680, 450, True)
    # showSprite(walk)

nextFrame = clock()
print("nextFrame:", nextFrame)
frame = 0

stoped = stopedCharacter()
showSprite(stoped.idle)

while True:
    if keyPressed("right"):
        walking = walkCharacter()
        if clock() > nextFrame:
            walking.walkImage += 1
            if walking.walkImage > 19:
                walking.walkImage = 0
            changeSpriteImage(walking.walk, walking.walkImage)
            nextFrame = clock() + 60

        # idleX += 7
        if walking.walkX > 1280:
            walking.walkX = -20

        moveSprite(walking.walk, walking.walkX, 450, True)
    else:
        stoped = stopedCharacter()
        if clock() > nextFrame:
            stoped.idleImage += 1
            if stoped.idleImage > 15:
                stoped.idleImage = 0
            changeSpriteImage(stoped.idle, stoped.idleImage)
            nextFrame = clock() + 60

        moveSprite(stoped.idle, 680, 450, True)
