
def getRequiredString(prompt, error):
    x = input(prompt)
    while x == "" or x.isspace():
        
        
        
    '''
Prompt the user until they provide a non-empty that is also not whitespace
   prompt - the text to show to the user as a prompt
   error - the error message to show the user on invalid entries
 returns a valid string
    '''
    # Implement me!
    return ""

def getIntegerInput(prompt, error):
    '''
Prompt the user until they provide valid integer value
   prompt - the text to show to the user as a prompt
   error - the error message to show the user on invalid entries
 returns an integer
    '''
    # Implement me!
    return 0    

def getPositiveIntegerInput(prompt, error):
    '''
Prompt the user until they provide valid positive value
   prompt - the text to show to the user as a prompt
   error - the error message to show the user on invalid entries
 returns a positive integer
    '''
    # Implement me!
    return 0    

def getFloatInput(prompt, error):
    '''
Prompt the user until they provide valid floating point number
   prompt - the text to show to the user as a prompt
   error - the error message to show the user on invalid entries
 returns a floating point number
    '''
    # Implement me!
    return 0    

def getMinimumIntegerInput(prompt, min, error):
    '''
Prompt the user until they provide an integer greater than or equal to the minimum
   prompt - the text to show to the user as a prompt
   min - the minimal value the user can enter
   error - the error message to show the user on invalid entries
 returns an integer greater than or equal to min
    '''
    # Implement me!
    return 0    

def getSeveralIntegers(prompt, count, error):
    '''
Prompt the user until they provide a predetermined number of integer values
        e.g.,  if you passed in "Test Score " this function would prompt
            Test Score 1:
            Test Score 2:
            Test Score ....(up to the count)
   prompt - the text to show to the user as a prompt
   count - the number of values to collect
   error - the error message to show the user on invalid entries
 returns a Python list of the entered values
    '''
    # Implement me!
    answers = []
    return answers
    


import subprocess
def testValidation():
    '''

    '''
    success = True
    tests = [# Happy Path
             ("purple\n13\n46\n3.14159\n1900\n1\n2\n3\n",
              ["I love purple", "I hope the lottery includes 13",
               "You look good for 46", "Not bad at 3.14159",
               "Are you sure that you are 46 if you were born in 1900",
               "Your lottery picks are: [1, 2, 3]"]),

             # Empty required
             ("\nbetter\n13\n46\n3.14159\n1900\n1\n2\n3\n",
              ["Input is required", "I love better"]),

             # Blank required
             ("  \nbetter\n13\n46\n3.14159\n1900\n1\n2\n3\n",
              ["Input is required", "I love better"]),

             # Invalid integer
             ("purple\nd\n13\n46\n3.14159\n1900\n1\n2\n3\n",
              ["You must provide an integer value", "I hope the lottery includes 13"]),
             
             # Negative integer
             ("purple\n13\n-1\n46\n3.14159\n1900\n1\n2\n3\n",
              ["You must provide a positive integer value", "You look good for 46"]),

             # Invalid Float
             ("purple\n13\n46\npi\n3.14159\n1900\n1\n2\n3\n",
              ["You must provide an float value", "Not bad at 3.14159"]),
             
             # Too Small Int
             ("purple\n13\n46\npi\n3.14159\n50\n1900\n1\n2\n3\n",
              ["Your integer must be greater than " + str(1900), "Are you sure that you are 46 if you were born in 1900"]),

             # Invalid multiple
             ("purple\n13\n46\npi\n3.14159\n50\n1900\n1\nd\n2\nf\n3\n",
              ["An integer is required", "Your lottery picks are: [1, 2, 3]"])
             ]
    for inputs, expected in tests:
        uut = subprocess.Popen('python validation.py -test'.split(),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        output, err = uut.communicate(inputs.encode(), 1)
        result = str(output)
        for item in expected:
            if result.find(item) == -1:
                success = False
                print("...... Test Failed......",
                      "The automated tester sent the inputs:", inputs,
                      "and expected your code to return:", item,
                      "but instead your code returned (the last value):", result, sep='\n')
                break

    return success

import sys
if len(sys.argv) == 1: #Ignore this for the automated tester, which adds a parameter
    if testValidation():
        print("Your validation passed the automated tests!")
    print(".....................")
    print("Now manually test your code")
    print()

favoriteColor = getRequiredString("What is your favorite color: ",
                                  "Input is required")
print("I love", favoriteColor)

luckyNumber = getIntegerInput("Your lucky number: ",
                              "You must provide an integer value")
print("I hope the lottery includes", luckyNumber)

age = getPositiveIntegerInput("Your age: ",
                              "You must provide a positive integer value")
print("You look good for", age)

pi = getFloatInput("How many digits of pi can you remember: ",
                   "You must provide an float value")
print ("Not bad at", pi)

year = getMinimumIntegerInput("Birth year: ", 1900,
                              "Your integer must be greater than " + str(1900))
print("Are you sure that you are", age, "if you were born in", year)

lottery = getSeveralIntegers("Pick a number ", 3, "An integer is required")
print("Your lottery picks are:", lottery)
