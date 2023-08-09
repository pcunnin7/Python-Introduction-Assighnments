from graphics import *

def main ():
    win = GraphWin ("Fall is Here", 1000, 800)
    
    sky = Rectangle(Point(0, 0), Point (1000, 800))
    sky.setFill("red")
    sky.draw(win)

    sun = Circle(Point(0, 105), 200)
    sun.setFill("Orange")
    sun.draw(win)

    grass = Rectangle(Point(0,500), Point(1000, 800))
    grass.setFill("darkgreen")
    grass.draw(win)

    base = Rectangle(Point(600,200), Point(800,500))
    base.setFill("navy")
    base.draw(win)

    windowoutline1 = Circle(Point(650, 250), 25)
    windowoutline1.setFill("grey")
    windowoutline1.draw(win)
   
    window1 = Circle(Point(650, 250), 23)
    window1.setFill("orange")
    window1.draw(win)

    windowoutline2 = Circle(Point(750, 250), 25)
    windowoutline2.setFill("grey")
    windowoutline2.draw(win)

    window2 = Circle(Point(750, 250), 23)
    window2.setFill("orange")
    window2.draw(win)

    door = Rectangle(Point(675, 450), Point(725, 500))
    door.setFill("Brown")
    door.draw(win)
    
    


main()
