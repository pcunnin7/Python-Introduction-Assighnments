SOLID              = 0
FREEZING_MELTING   = 1
LIQUID             = 2
BOILING_CONDENSING = 3
GAS                = 4

# ...................... 1 .....................................
def determineState(currentTemp):
    '''
Given the temperature, determine the state of matter
    currentTemp - the current temperature
 returns one of the defined constants for the states of matter above
    '''
    FREEZING_POINT = 0
    BOILING_POINT = 100
    THRESHOLD = 3
    if currentTemp < FREEZING_POINT + THRESHOLD:
        return FREEZING_MELTING
    elif currentTemp > BOILING_POINT  - THRESHOLD:
        return BOILING_CONDENSING
    elif currentTemp < FREEZING_POINT - THRESHOLD:
        return SOLID
    elif currentTemp > BOILING_POINT + THRESHOLD:
        return GAS
    else:
        return LIQUID

# ...................... 2 .....................................
# Your alternative version of the logic that must be different from the final answer above
# Hint: There are many ways to order if/else/elif logic.  Pick any of the elif/else
#  cases as a new starting point and write the entire logic structure from there
def determineStateAlternative(currentTemp):
    '''
Given the temperature, determine the state of matter
    currentTemp - the current temperature
 returns one of the defined constants for the states of matter above
    '''
    return 5 # 5 is invalid for every case, you must replace!

#==================================================================
# Everything below here is tester code DO NOT MODIFY
LABELS = ["Solid", "Freezing/Melting", "Liquid", "Boilding/Condensing", "Gas", "Unknown"]
TEST_CASES = { -10 : 0, -3 : 1, 3 : 1, 50 : 2, 97 : 3, 103 : 3, 110 : 4}

def stateTester(using):
    '''
 Test the determineState function(s)
   using - this parameter is the function to be tested.  Python allows you to store a function
           as a variable.  Since 'my' and 'your' functions use the same parameters and only have
           a different name, the same tester can test both of them using this parameter
    '''
    passed = True
    for temperature in TEST_CASES:
        result = using(temperature)
        if result != TEST_CASES[temperature]:
            passed = False
            print ("Fail: expected", LABELS[TEST_CASES[temperature]], "got", LABELS[result], "for", temperature)
    if passed:
        print("All tests passed using ", using)

# Only run this code below if this is called as the main, not imported
if __name__ == '__main__':
    print("................................................")
    print("Test your fix to my original code")
    stateTester(determineState)

    print("\n................................................")
    print("Test your alternative")
    stateTester(determineStateAlternative)
