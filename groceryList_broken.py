def groceryList():
    print("Basic Grocery List Pricing Tool")

    milkPrice = eval(input("Gallon of Milk: $"))
    quantity1 = eval(input("Number of gallons: "))

    eggPrice  = eval(input("Carton of eggs: $"))
    quantity2 = eval(input("Number of cartons: "))
    
    lPrice    = eval(input("Loaf of bread: $"))
    quantity3 = eval(input("Number of loaves: "))

    sushi     = eval(input("Sushi tray: $"))
    quantity4 = eval(input("Number of trays: "))

    print("Grocery List")
    print("------------")
    print("Milk - ", quantity1, '@', "$" + str(milkPrice))
    print("Sushi - ", quantity4, '@', "$" + str(sushi))
    print("Bread - ", quantity3, '@', "$" + str(lPrice))
    print("Eggs - ", quantity2, '@', "$" + str(eggPrice))

    totalCost = (milkPrice * quantity1)
    totalCost += (eggPrice * quantity2)
    totalCost += (lPrice * quantity3)
    totalCost += (sushi * quantity4)
    x = round(totalCost, 2) 


    itemCount = quantity1 + quantity2 + quantity3 + quantity4;
    print("Total: $" + str(x), "for ", itemCount, 'items')
        
#=============================================================
# Testing code below - DO NOT EDIT
import subprocess
def testGroceryList():
    '''
Test the user interface for the grocery list.  The test assumes the code prompts the
user for the following field in this exact order:
  1.) Cost of a gallon of milk
  2.) Number of gallons purchased
  3.) Cost of a carton of eggs
  4.) Number of carts purchased
  5.) Cost for a loaf of bread
  6.) Number of loaves purchased
  7.) Cost for a tray of sushi
  8.) Number of trays purchased
    '''
    success = True
    tests = [("2.19\n2\n.99\n3\n1.15\n1\n7.88\n2\n",
              ["Milk -  2 @ $2.19", "Sushi -  2 @ $7.88", "Bread -  1 @ $1.15",
               "Eggs -  3 @ $0.99", "Total: $24.26 for  8 items"]),
             ("1.77\n1\n1.05\n6\n3.99\n2\n25.13\n1\n",
              ["Milk -  1 @ $1.77", "Sushi -  1 @ $25.13", "Bread -  2 @ $3.99",
               "Eggs -  6 @ $1.05", "Total: $41.18 for  10 items"])]
    for inputs, expected in tests:
        uut = subprocess.Popen('python3 groceryList_broken.py -test'.split(),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        output, err = uut.communicate(inputs.encode(), 1)
        result = str(output)
        for item in expected:
            if result.find(item) == -1:
                print("!!")
                print(item)
                print("!!")
                success = False
                print("...... Test Failed......",
                      "The automated tester sent the inputs:", inputs,
                      "and expected your code to return:", expected,
                      "but instead your code returned (the last value):", result, sep='\n')
                break

    return success

import sys
if len(sys.argv) == 1: #Ignore this for the automated tester, which adds a parameter
    if testGroceryList():
        print("Your grocery list passed the automated tests!")
    print(".....................")
    print("Now manually test your code")
    print()
   
groceryList()
