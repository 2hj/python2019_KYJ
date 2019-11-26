from pygame_functions import *

screenSize(1000, 750)
setBackgroundImage("background.png")

girl = makeSprite("girl.png")
showSprite(girl)

xPos = 500
yPos = 320
xSpeed = 0
ySpeed = 0

moveSprite(girl, xPos, yPos)

while True:
    if keyPressed("up"):
        rotateSprite(girl, 0)
        ySpeed -= 2
    elif keyPressed("down"):
        rotateSprite(girl, 180)
        ySpeed += 2
    elif keyPressed("right"):
        rotateSprite(girl, 90)
        xSpeed += 2
    elif keyPressed("left"):
        rotateSprite(girl, -90)
        xSpeed -= 2

    xPos += xSpeed
    if xPos > 960:
        xPos = -100
    elif xPos < -100:
        xPos = 960

    yPos += ySpeed
    if yPos > 700:
        yPos = -100
    elif yPos < -100:
        yPos = 700

    moveSprite(girl, xPos, yPos)

    tick(30)

endWait()
