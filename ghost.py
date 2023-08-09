from graphics import *
import math
import time

def drawGhost(win, getx, gety, bodyColor = 'white', eyeColor = 'black', scalar = 1):
    ghostParts = []
    ghostHead = Circle(Point(getx,gety), (100*scalar))
    ghostHead.setFill(bodyColor)
    ghostHead.draw(win)
    ghostParts.append(ghostHead)

    ghostBody = Rectangle(Point(getx-(100*scalar),gety), Point(getx+(100*scalar), gety+(200*scalar)))
    ghostBody.setFill(bodyColor)
    ghostBody.setOutline(bodyColor)
    ghostBody.draw(win)
    ghostParts.append(ghostBody)

    leftPoint1   = Point(getx-(100*scalar), gety+(200*scalar))
    bottomPoint1 = Point(getx-(75*scalar), gety+(230*scalar))
    rightPoint1  = Point(getx-(50*scalar), gety+(200*scalar))

    triangle1   = Polygon(leftPoint1, rightPoint1, bottomPoint1)
    triangle1.setFill(bodyColor)
    triangle1.setOutline(bodyColor)
    triangle1.draw(win)
    ghostParts.append(triangle1)

    leftPoint2   = Point(getx-(50*scalar), gety+(200*scalar))
    bottomPoint2 = Point(getx-(25*scalar), gety+(230*scalar))
    rightPoint2  = Point(getx, gety+(200*scalar))

    triangle2   = Polygon(leftPoint2, rightPoint2, bottomPoint2)
    triangle2.setFill(bodyColor)
    triangle2.setOutline(bodyColor)
    triangle2.draw(win)
    ghostParts.append(triangle2)

    leftPoint3   = Point(getx, gety+(200*scalar))
    bottomPoint3 = Point(getx+(25*scalar), gety+(230*scalar))
    rightPoint3  = Point(getx+(50*scalar), gety+(200*scalar))

    triangle3   = Polygon(leftPoint3, rightPoint3, bottomPoint3)
    triangle3.setFill(bodyColor)
    triangle3.setOutline(bodyColor)
    triangle3.draw(win)
    ghostParts.append(triangle3)

    leftPoint4   = Point(getx+(50*scalar), gety+(200*scalar))
    bottomPoint4 = Point(getx+(75*scalar), gety+(230*scalar))
    rightPoint4  = Point(getx+(100*scalar), gety+(200*scalar))

    triangle4   = Polygon(leftPoint4, rightPoint4, bottomPoint4)
    triangle4.setFill(bodyColor)
    triangle4.setOutline(bodyColor)
    triangle4.draw(win)
    ghostParts.append(triangle4)

    leftEye = Oval(Point(getx-(55*scalar), gety-(20*scalar)), Point(getx-(25*scalar), gety+(20*scalar)))
    leftEye.setFill(eyeColor)
    leftEye.draw(win)
    ghostParts.append(leftEye)
    
    rightEye = Oval(Point(getx+(25*scalar), gety-(20*scalar)), Point(getx+(55*scalar), gety+(20*scalar)))
    rightEye.setFill(eyeColor)
    rightEye.draw(win)
    ghostParts.append(rightEye)

    return ghostParts

def animate(objectList, startXPosition):
    xVelocity = 4
    while True:
        if startXPosition >=  900:
            xVelocity = -4
        elif startXPosition <= 100:
            xVelocity = 4

        yVelocity = 2 * math.sin(startXPosition / 20)

        for part in objectList:
            part.move(xVelocity, yVelocity)
        startXPosition = startXPosition + xVelocity
        time.sleep(1/30)
    

def main():
    win = GraphWin("Messy Ghost", 1000, 700)
    background = Rectangle(Point(0,0), Point(1000, 700))
    background.setFill("black")
    background.draw(win)
    ghost2 = drawGhost(win, 300, 400, 'white', 'black', .5)
    ghost3 = drawGhost(win, 150, 150, 'white', 'black', .5)
    ghost4 = drawGhost(win, 800, 175, 'white', 'black', .5)
    ghost5 = drawGhost(win, 750, 600, 'white', 'black', .5)
    ghost6 = drawGhost(win, 900, 350, 'white', 'black', .5)
    ghost7 = drawGhost(win, 575, 200, 'white', 'black', .5)
    ghost8 = drawGhost(win, 425, 575, 'white', 'black', .5)
    ghost9 = drawGhost(win, 170, 350, 'white', 'black', .5)
    ghost10 = drawGhost(win, 115, 600, 'white', 'black', .5)
    ghost11 = drawGhost(win, 480, 340, 'white', 'black', .5)
    ghost1 = drawGhost(win, 500, 100, 'yellow', 'purple')
    animate(ghost1, 500)
   

main()
