from graphics import *
import time

def drawBackground(win, time):
    if time == 'evening':
        skyColor = 'navy'
    elif time == 'night':
        skyColor = 'black'
    else:
        skyColor = "skyblue"
    sky = Rectangle(Point(0, 0), Point(win.width, win.height))
    sky.setFill(skyColor)
    sky.draw(win)

    grass = Rectangle(Point(0, 200), Point(win.width, win.height))
    grass.setFill("green")
    grass.draw(win)

def drawRoad(win):

    road = Rectangle(Point(0, 300), Point(win.width, 500))
    road.setFill("black")
    road.draw(win)

    solid1 = Rectangle(Point(0, 390), Point(win.width, 395))
    solid1.setFill('yellow')
    solid1.draw(win)

    solid2 = Rectangle(Point(0, 400), Point(win.width, 405))
    solid2.setFill('yellow')
    solid2.draw(win)

    for start in range(0, win.width + 20, 80):
        dash1 = Rectangle(Point(start, 350), Point(start + 40, 355))
        dash1.setFill('yellow')
        dash1.draw(win)
        dash2 = Rectangle(Point(start, 450), Point(start + 40, 455))
        dash2.setFill('yellow')
        dash2.draw(win)

def drawTruck(win, atX, atY, color):
    truckParts = []
    truckBody = Rectangle(Point(atX, atY), Point(atX + 100, atY + 50))
    truckBody.setFill(color)
    truckBody.draw(win)
    truckParts.append(truckBody)

    truckCab = Polygon(Point(atX + 100, atY + 10), Point(atX + 120, atY + 10),
                       Point(atX + 127, atY + 25), Point(atX + 145, atY + 27),
                       Point(atX + 145, atY + 50), Point(atX + 100, atY + 50))
    truckCab.setFill(color)
    truckCab.draw(win)
    truckParts.append(truckCab)

    window = Polygon(Point(atX + 104, atY + 14), Point(atX + 118, atY + 14),
                     Point(atX + 123, atY + 25), Point(atX + 104, atY + 25))
    window.setFill("grey")
    window.draw(win)
    truckParts.append(window)

    backTire = drawTire(win, atX + 20, atY + 50)
    midTire = drawTire(win, atX + 84, atY + 50)
    frontTire = drawTire(win, atX + 127, atY + 50)
    truckParts.extend(backTire)
    truckParts.extend(midTire)
    truckParts.extend(frontTire)
    return truckParts

def drawTire(win, atX, atY):
    rimsize = 10
    Tire = Circle(Point(atX, atY), rimsize)
    Tire.setFill('black')
    Tire.setOutline('grey')
    Tire.draw(win)
    Rim = Circle(Point(atX, atY), rimsize * .6)
    Rim.setFill('silver')
    Rim.draw(win)
    return [Tire, Rim]

def move(objectList, x, y):
         for shape in objectList:
            shape.move(x,y)

def main():
    win = GraphWin('Traffic', 800, 750)
    drawBackground(win, 'night')
    drawRoad(win)
    truck = drawTruck(win, 20, 390, 'white')
    truck2 = drawTruck(win, 200, 420, 'purple')
    for frames in range(300):
        time.sleep(1/30)
        move(truck, 15, 0)
        move(truck2,5,0)
    

    

main()



