from graphics import *

def drawRightTriangle(win, rightAnglePoint, baseLength, heightLength):
    topPoint = Point(rightAnglePoint.getX(),
                     rightAnglePoint.getY() - baseLength)
    rightPoint = Point(rightAnglePoint.getX() + heightLength,
                       rightAnglePoint.getY())
    base = Line(rightAnglePoint, topPoint)
    height = Line(rightAnglePoint, rightPoint)
    hypotenuse = Line(topPoint. rightPoint)
    base.draw(win)
    height.draw(win)
    hypotenuse.draw(win)
    pass

def drawIsoscelesTriangle(win, topPoint, base, height):
    '''
Draw an isoscelese triangle using lines starting at the topPoint with the provided base and height
   win – the graphics window where this function draws the shape
   topPoint - The top point of the triangle
   base – The length of the base of the triangle
   height – The length for the height of the triangle
    '''
    pass

def drawDiamond(win, topPoint, width, height):
    '''
Draw a diamond using lines starting at the topPoint with the provided width and height
   win – the graphics window where this function draws the shape
   topPoint - The top point of the shape
   width – The length of the width of the shape
   height – The length for the height of the shape
    '''
    pass

def drawStar5(win, topPoint, width, height):
    '''
Draw a five-pointed star using lines starting at the topPoint with the provided width and height
   win – the graphics window where this function draws the shape
   topPoint - The top point of the shape
   width – The length of the width of the shape
   height – The length for the height of the shape
    '''
    pass

def drawPentagon(win, topPoint, width, height):
    '''
Draw a pentagon using lines starting at the topPoint with the provided width and height
   win – the graphics window where this function draws the shape
   topPoint - The top point of the shape
   width – The length of the width of the shape
   height – The length for the height of the shape
    '''
    pass

def drawStar6(win, topPoint, width, height):
    '''
Draw a six-pointed star using lines starting at the topPoint with the provided width and height
   win – the graphics window where this function draws the shape
   topPoint - The top point of the shape
   width – The length of the width of the shape
   height – The length for the height of the shape
    '''
    pass

def drawHexagon(win, topPoint, width, height):
    '''
Draw a hexagon using lines starting at the topPoint with the provided width and height
   win – the graphics window where this function draws the shape
   topPoint - The top point of the shape
   width – The length of the width of the shape
   height – The length for the height of the shape
    '''
    pass

#=============================================================
# Testing code below - DO NOT EDIT
def main():
    '''
Tests the shape drawings in a single display
    '''
    win = GraphWin('Polygons', 600, 270)

    drawRightTriangle(win, Point(15, 110), 100, 100)
    drawIsoscelesTriangle(win, Point(200, 10), 100, 100)
    drawDiamond(win, Point(350, 10), 100, 100)
    drawStar5(win, Point(65, 150), 100, 100)
    drawStar6(win, Point(200, 150), 100, 100)
    drawPentagon(win, Point(350, 150), 100, 100)
    drawHexagon(win, Point(500, 150), 100, 100)
    
# Only run this code below if this is called as the main, not imported
if __name__ == '__main__':
    main()
