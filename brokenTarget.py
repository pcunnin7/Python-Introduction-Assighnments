import time
import math
from graphics import *

MISS     = 0
BULLSEYE = 1
RING1    = 2
RING2    = 3
RING3    = 4
RING4    = 5

TARGET_CENTER = Point(100, 75)
RADIUS = [0, 15, 30, 45, 60, 75, 90]
RADIUS_COLOR = ['black', 'red', 'white', 'blue', 'white', 'red']

#...................... 1 ......................................
# The animated arrow is missing the target.  Help me to adjust
# the code between the lines below so that the arrow hits the target!
def main():
    '''
Main Program to draw a target and arrow onto a window
    '''
    # Build the window with the title and size specified
    win = GraphWin('Target', 200, 150)

    #-------------------------------------
    arrowLocation = Point(200, 75)
    for arrowX in range(int(arrowLocation.getX()), 100, -10):
        background = Rectangle(Point(0, 0), Point(win.getWidth(), win.getHeight()))
        background.setFill('light grey')
        background.draw(win)
        
        drawTarget(win, MISS)

        arrowLocation = Point (arrowX, arrowLocation.getY())
        drawArrow(win, arrowLocation)
        time.sleep(1/30)
        
    #-------------------------------------

    #Draw it one list time to reflect where it hit
    drawTarget(win, determineHit(arrowLocation))
    drawArrow(win, arrowLocation)


#........................ 2 .........................
# Replace the code between the lines with loop instead of the if/else logic
def determineHit(strikePoint):
    '''
Determine where on the target the strike points hit
   strikePoint - the impact of the arrow
 returns one of the constants above
    '''
    x = strikePoint.getX()
    y = strikePoint.getY()
    z = 0

    distance = math.sqrt((TARGET_CENTER.getX() - x)**2 + (TARGET_CENTER.getY() - y)**2)
    #-------------------------------------
    for radius in reversed(RADIUS):
        if distance > radius:
            z += 1

    return z
    
    #if distance < RADIUS[BULLSEYE]:
            #return BULLSEYE
    #elif distance < RADIUS[RING1]:
        #return RING1
    #elif distance < RADIUS[RING2]:
        #return RING2
    #elif distance < RADIUS[RING3]:
        #return RING3
    #elif distance < RADIUS[RING4]:
        #return RING4
    #else:
        #return MISS
    #-------------------------------------

#........................ 3 .........................
# We can refactor the code we wrote last time to make it more flexible.
# Rewrite the drawTarget function to use a loop instead of a long if/else chain
def drawTarget(win, hit):
    '''
Draw a ringed target onto the provided window
  win - the target window for the arrow
  hit - the index of the ring that was hit (using constants above)
    '''
    ring4 = Circle(TARGET_CENTER, RADIUS[RING4])
    if hit == RING4:
        ring4.setFill("green")
    else:
        ring4.setFill("red")
    ring4.draw(win)

    ring3 = Circle(TARGET_CENTER, RADIUS[RING3])
    if hit == RING3:
        ring3.setFill("green")
    else:
        ring3.setFill("white")
    ring3.draw(win)

    ring2 = Circle(TARGET_CENTER, RADIUS[RING2])
    if hit == RING2:
        ring2.setFill("green")
    else:
        ring2.setFill("blue")
    ring2.draw(win)

    ring1 = Circle(TARGET_CENTER, RADIUS[RING1])
    if hit == RING1:
        ring1.setFill("green")
    else:
        ring1.setFill("white")
    ring1.draw(win)

    bullseye = Circle(TARGET_CENTER, RADIUS[BULLSEYE])
    if hit == BULLSEYE:
        bullseye.setFill("green")
    else:
        bullseye.setFill("red")
    bullseye.draw(win)


    
def drawArrow(win, startPoint):
    '''
Draw an arrow onto the provided window
  win - the target window for the arrow
  startPoint - where to draw the tip of the arrow
    '''
    x = startPoint.getX()
    y = startPoint.getY()
    head = Polygon(Point(x, y), Point(x + 13, y - 5), Point(x + 13, y + 5))
    head.setFill("grey")
    head.draw(win)

    shaft = Line(Point(x + 60, y), Point(x + 13, y))
    shaft.setWidth(3)
    shaft.setOutline("brown")
    shaft.draw(win)

    fletching = Polygon(Point(x + 60, y), Point(x + 65, y - 5), Point(x + 85, y - 5),
                        Point(x + 80, y), Point(x + 85, y + 5), Point(x + 65, y + 5))
    fletching.setFill("yellow")
    fletching.draw(win)

main()
