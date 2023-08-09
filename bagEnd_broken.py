from graphics import *

def main():
    win = GraphWin('Bag End', 200, 150) # give title and dimensions

    sky = Rectangle(Point(0, 0), Point(200, 200))
    sky.setFill("skyblue")
    sky.draw(win)

    hill = Oval(Point(-100, 50), Point(300,400))
    hill.setFill("green")
    hill.draw(win)

    house = Rectangle(Point(25, 75), Point(175, 150))
    house.setFill(color_rgb(120, 95, 10))
    house.draw(win)

    window1 = Circle (Point(48, 105), 10)
    window1.setFill("blue")
    window1.draw(win)

    window2 = Circle (Point(152, 105), 10)
    window2.setFill("blue")
    window2.draw(win)

    door = Circle(Point(100, 120), 29)
    door.setFill(color_rgb(10, 75, 10))
    door.draw(win)

    doorknob = Circle(Point(100, 120), 4)
    doorknob.setFill(color_rgb(10, 55, 10))
    doorknob.draw(win)

    ring1 = Circle(Point(100, 128), 2)
    ring1.setOutline("gold")
    ring1.draw(win)

    ring2 = Circle(Point(100, 132), 2)
    ring2.setOutline("gold")
    ring2.draw(win)

    ring3 = Circle(Point(96, 132), 2)
    ring3.setOutline("gold")
    ring3.draw(win)

    ring4 = Circle(Point(104, 132), 2)
    ring4.setOutline("gold")
    ring4.draw(win)

    ring5 = Circle(Point(100, 136), 2)
    ring5.setOutline("gold")
    ring5.draw(win)

    ring6 = Circle(Point(96, 136), 2)
    ring6.setOutline("gold")
    ring6.draw(win)

    ring7 = Circle(Point(92, 136), 2)
    ring7.setOutline("gold")
    ring7.draw(win)

    ring8 = Circle(Point(88, 136), 2)
    ring8.setOutline("gold")
    ring8.draw(win)

    ring9 = Circle(Point(104, 136), 2)
    ring9.setOutline("gold")
    ring9.draw(win)

    ring10 = Circle(Point(108, 136), 2)
    ring10.setOutline("gold")
    ring10.draw(win)

    ring11 = Circle(Point(112, 136), 2)
    ring11.setOutline("gold")
    ring11.draw(win)

    ring12 = Circle(Point(100, 140), 2)
    ring12.setOutline("gold")
    ring12.draw(win)

    ring13 = Circle(Point(96, 140), 2)
    ring13.setOutline("gold")
    ring13.draw(win)

    ring14 = Circle(Point(92, 140), 2)
    ring14.setOutline("gold")
    ring14.draw(win)

    ring15 = Circle(Point(88, 140), 2)
    ring15.setOutline("gold")
    ring15.draw(win)

    ring16 = Circle(Point(84, 140), 2)
    ring16.setOutline("gold")
    ring16.draw(win)

    ring17 = Circle(Point(104, 140), 2)
    ring17.setOutline("gold")
    ring17.draw(win)

    ring18 = Circle(Point(108, 140), 2)
    ring18.setOutline("gold")
    ring18.draw(win)

    ring19 = Circle(Point(112, 140), 2)
    ring19.setOutline("gold")
    ring19.draw(win)

    ring20 = Circle(Point(116, 140), 2)
    ring20.setOutline("gold")
    ring20.draw(win)


main()
