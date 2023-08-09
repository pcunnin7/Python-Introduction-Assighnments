def promptUserForDogTest():
    name           = ''
    color          = ''
    favoriteNumber = ''
    car            = ''
    spicyFood      = ''
    
    # ................................
    # Do not to modify any of the code outside of the dotted lines.

    # Add code to prompt the user for each of the variables required to
    # complete the online dog test.  The exact text you show the user 
    # should look like, but does not have to exactly match the
    # example, but you need to fill all of the variables in the order specified.

    # As a tip, fill one variable at a time and test that manually.
    # Don't try to write all the code at once to satisfy the automated tester!


    name = input("What is your name ")
    color = input("What is your favorite color ")
    favoriteNumber = input("What is your favorite number ")
    car = input("What was your first car ")
    spicyFood = input("What is the spiciest food you like to eat ")


    
    # Do not to modify any of the code outside of the dotted lines.
    # ................................
    
    dogBreed = dogTest (name, color, favoriteNumber, car, spicyFood)
    print(dogBreed)

def dogTest(name, color, favoriteNumber, car, spicyFood):
    '''
Calculate the dog breed for the inputs
   name - The test taker's name
   color - Their favorite color
   favoriteNumber - Their favorite number
   car - Their favorite vehicle
   spicyFood - Their favorite spicy food
 returns the breed of dog they would have been born as
    '''
    if color == "blue":
        return "Irish Wolfhound"
    elif color == "gold":
        return "Golden Retriever"
    elif color == "white":
        return "Great Pyranese"
    elif color == "purple":
        return "Newfoundland"
    elif color == "brown":
        return "Beagle"
    elif color == "black":
        return "Rottweiler"
    elif color == "grey":
        return "Greyhound"
    elif color == "yellow":
        return "Labrador"
    elif color == "spotted":
        return "Dalmation"
    elif color == "orange":
        return "Chow Chow"
    else:
        return "Mixed Breed"

#=============================================================
# Testing code below - DO NOT EDIT
import subprocess
def testDogTest():
    '''
Test the user interface for the dog test.  The test assumes the code prompts the
user for the following field in this exact order:
  1.) Name
  2.) Favorite Color
  3.) Favorite Number
  4.) Favorite Vehicle
  5.) Favorite Spicy Food
    '''
    success = True
    tests = [("Chien\norange\n42\nPrius\nCurry\n", "Chow Chow"),
             ("Tony\npurple\n13\nHummer\nMarie Sharps\n", "Newfoundland"),
             ("Kelly\nbrown\n9\nJeep\nMartin's BBQ Chips\n", "Beagle")]
    for inputs, expected in tests:
        uut = subprocess.Popen('python3 dogTest.py -test'.split(),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        output, err = uut.communicate(inputs.encode(), 1)
        result = str(output)
        if result.find(expected) == -1:
            success = False
            print("...... Test Failed......",
                  "The automated tester sent the inputs:", inputs,
                  "and expected your code to return:", expected,
                  "but instead your code returned (the last value):", result, sep='\n')

    return success

import sys
if len(sys.argv) == 1: #Ignore this for the automated tester, which adds a parameter
    if testDogTest():
        print("Your dog test passed the automated tests!")
    print(".....................")
    print("Now manually test your code")
    print()

promptUserForDogTest()
