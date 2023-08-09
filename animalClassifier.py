# From: https://www.researchgate.net/publication/315146311_ANIMAL_CLASSIFICATION_IN_WILDLIFE_THROUGH_IMAGES_USING_STATISTICAL_METHODS_AND_DECISION_TREE

AMPHIBIAN = "Amphibian"
BIRD      = "Bird"
FISH      = "Fish"
INSECT    = "Insect"
MAMMAL    = "Mammal"
REPTILE   = "Reptile"

#....................... 2 ..............................
# Modify the following data structure to match your defined test cases.  
# The inputs to the test cases are next represented by Boolean values
#  (must be True and False, case sensitive)
# that align to one of the input values in the following order:
#                          skeleton, wings, feathers, eggs,  milk,  meta,  gills
TEST_CASES = [[INSECT    , [False,    False, False,    False, False, False, False]],
              [BIRD      , [False,    False, False,    False, False, False, False]],
              [MAMMAL    , [False,    False, False,    False, False, False, False]],
              [MAMMAL    , [False,    False, False,    False, False, False, False]],
              [AMPHIBIAN , [False,    False, False,    False, False, False, False]],
              [REPTILE   , [False,    False, False,    False, False, False, False]],
              [FISH      , [False,    False, False,    False, False, False, False]]]

# The following code, AnimalClassifier, is a class.  It helps to group data
# and is a vital part of Object-Oriented programming.  We won't do a lot with
# classes in this course, but they are important later.  For now, it is just a way
# of grouping the various properties to classify an animal.
class AnimalClassifier:
    hasSkeleton = False
    hasWings    = False
    hasFeathers = False
    laysEggs    = False
    drinksMilk  = False
    undergoesMetamorphasis = False
    hasGills   = False

#...................  3  ..........................................
    def classify(self):
        '''
Use the attributes of the Animal Classifier task to determine the animal
   self - an grouping of the AnimalClassifier attributes
 returns the class of the animal with those properties
        '''
        if self.hasSkeleton:
            if self.hasWings:
                if self.hasFeathers:
                    return BIRD
                else:
                    return MAMMAL
            else:
                if not self.laysEggs:
                    if self.drinksMilk:
                        return MAMMAL
                if self.undergoesMetamorphasis:
                    return AMPHIBIAN
                else:
                    if self.hasGills:
                        return FISH
                    else:
                        return REPTILE
        else:
            return INSECT

#==================================================================
# Everything below here is tester code DO NOT MODIFY
    def __init__(self, skeleton, wings, feathers, eggs, milk, meta, gills):
        '''
Initializes the class with the provided values
        '''
        self.hasSkeleton = skeleton
        self.hasWings    = wings
        self.hasFeathers = feathers
        self.laysEggs    = eggs
        self.drinksMilk  = milk
        self.hasGills    = gills
        self.undergoesMetamorphasis = meta


def getBoolean(prompt):
    '''
Prompt the user a question that is answered true or false
   prompt - the text to ask the user
 returns True or False as specified by the user
    '''
    while True:
        answer = input(prompt).lower()
        if (answer == "true" or answer == 't'):
            return True
        elif (answer == "false" or answer == 'f'):
            return False
        else:
            print("You must answer True (t) or False (f)")

def presentToUser():
    '''
Ask the user a series of questions that help to classify the animal and
then show them the result
    '''
    hasSkeleton = getBoolean("Does your animal have a skeleton:")
    hasWings    = getBoolean("Does it have wings:")
    hasFeathers = getBoolean("Does it have feathers:")
    laysEggs    = getBoolean("Does it lay eggs:")
    drinksMilk  = getBoolean("Does its young drink milk:")
    undergoesMetamorphasis = getBoolean("Does it undergo a metamorphasis:")
    hasGills   = getBoolean("Does it have gills:")
        
    classifier = AnimalClassifier(hasSkeleton, hasWings, hasFeathers, laysEggs,
                                  drinksMilk, undergoesMetamorphasis, hasGills)
    print("Your animal is a", classifier.classify())

def testClassifier():
    '''
Test the classify logic using the test cases defined above
    '''
    success = True
    for testCase in TEST_CASES:
        answer     = testCase[0]
        parameters = testCase[1]
        test = AnimalClassifier(parameters[0], parameters[1], parameters[2], parameters[3],
                                parameters[4], parameters[5], parameters[6])
        result = test.classify()
        if result != answer:
            success = False
            print ("Test case Failed: I expected", answer, "but got", result, "for the inputs", parameters)
    return success

def testPlatypus():
    success = True
    answer = MAMMAL 
    parameters = [True, False, False, True, True, False, False]
    test = AnimalClassifier(parameters[0], parameters[1], parameters[2], parameters[3],
                            parameters[4], parameters[5], parameters[6])
    result = test.classify()
    if result != answer:
        success = False
        print ("Platypus Test case Failed: I expected", answer, "but got", result, "for the inputs", parameters)
    return success

if __name__ == '__main__':
    if testClassifier() and testPlatypus():
        print("All test cases passed!")
    print(".................")
    print("Classify your own animal now...")
    presentToUser()
