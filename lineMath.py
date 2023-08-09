def computeSlope(x1, y1, x2, y2):
    '''
Given two points, calculate the slope of a line between the two coordinantes
   x1 - the x dimention of the first point
   y1 - the y dimention of the first point
   x2 - the x dimention of the second point
   y2 - the y dimention of the second point
 returns the slope of the line
    '''
    return 0

def computeYIntercept(x1, y1, x2, y2):
    '''
Given two points, calculate the Y intercept of a line between the two coordinantes
   x1 - the x dimention of the first point
   y1 - the y dimention of the first point
   x2 - the x dimention of the second point
   y2 - the y dimention of the second point
 returns the slope of the line
    '''
    return 0
    

#=============================================================
# Testing code below - DO NOT EDIT
def testLineMath():
    '''
Test the computeSlope and computeYIntercept functions
    '''
    success = True
    tests = [([(1, 1), (2, 2)], (1, 0)),
             ([(5, 20), (10, 2)], (-3.6, 38)),
             ([(-25, 2), (-5, 16)], (0.7, 19.5)),
             ([(-10, 50), (100, 50)], (0, 50))]
    for inputs, expected in tests:
        m = computeSlope(inputs[0][0], inputs[0][1], inputs[1][0], inputs[1][1])
        b = computeYIntercept(inputs[0][0], inputs[0][1], inputs[1][0], inputs[1][1])
        if m != expected[0]:
            success = False
            print("...... computeSlope Failed......",
                  "The automated tester sent the inputs:\n", inputs,
                  "\n and expected your code to return:", expected[0],
                  "\nbut instead your code returned:", m)#, sep='')
        if b != expected[1]:
            success = False
            print("...... computeYIntercept Failed......",
                  "The automated tester sent the inputs:\n", inputs,
                  "\n and expected your code to return:", expected[1],
                  "\nbut instead your code returned:", b)#, sep='')
    return success

# Only run this code below if this is called as the main, not imported
if __name__ == '__main__':
    if testLineMath():
        print("Your Line Math passed!")
