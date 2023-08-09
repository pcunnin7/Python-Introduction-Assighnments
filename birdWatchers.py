import random

def addBirdSighting(birdSighting, ledger):
    '''
Add a bird sighting to the current day in the ledger
   birdSighting - the sighting to add
   ledger - the ledger to update
    '''
    print(birdSighting)
    day = []
    day.append(birdSighting)
    ledger.append(day)
    
    

def startNewDay(ledger):
    '''
Advance the ledger to start a new day of entries
   ledger - the ledger to advance
    ''' 
    ledger = []
    
def birdsSeenEachDay(ledger):
    '''
Compute the number of birds within the ledger for each day
   ledger - the ledger to analyze
 returns a list of counts, one for each day
    '''
    counts = []
    count = 0
    for entry in ledger:
        count += 1
    counts.append(count)
    return counts


def printLedger(ledger):
    '''
Print the sighting within the ledger, separated by the day
    '''

#===================================================================
# Test code below DO NOT MODIFY
BIRDS = ["Finch", "Robin", "Hummingbird", "Crow", "Eagle", "Hawk", "Cardinal", "Vulture", "Phoenix", "Sparrow"]
LOCATIONS = ["Park", "Backyard", "Skyscraper", "Forest", "Jungle", "Roadside", "Cage", "Sky", "Desert"]
TIME_OF_DAY = ["6-10AM", "10AM-2PM", "2-6PM", "6-10PM", "10PM-2AM", "2-6AM"]

def generateSighting():
    return BIRDS[random.randrange(len(BIRDS))], \
            LOCATIONS[random.randrange(len(LOCATIONS))], \
            TIME_OF_DAY[random.randrange(len(TIME_OF_DAY))]

def testLedger():
    ledger = []

    dayCount = []
    numberOfDays = random.randint(4, 6)
    print("The test cases will generate", numberOfDays, "days")
    for day in range(numberOfDays):
        startNewDay(ledger)
        numberOfSightings = random.randint(0, 5)
        dayCount.append(numberOfSightings)
        print("Day", day + 1, "will contain", numberOfSightings, "sightings")
        for count in range(numberOfSightings):
            sighting = generateSighting()
            addBirdSighting(sighting, ledger)

    counts = birdsSeenEachDay(ledger)
    if counts != dayCount:
        print("birdsSeenEachDay() Failed:  Your code returned", counts, "but I expected", dayCount)
    else:
        print("birdsSeenEachDay() Passed!")

    printLedger(ledger)

# Only run this code below if this is called as the main, not imported
if __name__ == '__main__':
    testLedger()
