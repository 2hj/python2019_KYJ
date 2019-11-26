from pygame_functions import *
from stoppedCharacter import StoppedCharacter
from walkCharacter import WalkCharacter

screenSize(1280, 900)
setBackgroundColour("dark green")

init = StoppedCharacter()

nextFrame = clock()
print("nextFrame:", nextFrame)
frame = 0


while True:
    print("clock():", clock())
    if clock() > nextFrame:
        init.idleImage += 1
    if init.idleImage > 15:
        init.idleImage = 0
    changeSpriteImage(init.idle, init.idleImage)
    nextFrame = clock() + 40

    moveSprite(init.idle, 680, 450, True)
