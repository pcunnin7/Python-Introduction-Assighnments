import random

debug = False
byBird = {}
byLocation = {}

#.......................... 1 ...........................
def addBirdSighting(day, birdSighting, ledger):
    '''
Add a bird sighting to the current day in the ledger
   birdSighting - the sighting to add
   ledger - the ledger to update
    '''
    if day in ledger:
        dailyLedger = ledger[day]
        dailyLedger.append(birdSighting)
    else:
        ledger[day] = [birdSighting]
    
    return ledger

#.......................... 2 ...........................
def birdsSeenEachDay(ledger):
    '''
Compute the number of birds within the ledger for each day
   ledger - the ledger to analyze
 returns a list of counts, one for each day
    '''
    counts = []
    return counts

#.......................... 3 ...........................
def printLedger(ledger):
    '''
Print the sighting within the ledger, separated by the day
   ledger - the ledger to print
    '''

#.......................... 4 ...........................
# Don't forget to fill the byBird dictionary in addBirdSighting!
def numberOfSightingsFor(bird, ledger):
    '''
Determine how many times the bird provided was sighted on the ledger (using a dictionary)
   bird - the bird to count
   ledger - the ledger to search
 returns the number of sightings for this bird in this ledger
    '''
    return 0

#.......................... 5 ...........................
# Don't forget to fill the byLocation dictionary in addBirdSighting!
def allBirdsSpottedAt(location, ledger):
    '''
Identify all unique species of birds spotted at the provided location and their count
   location - the location to query
   ledger - the ledger to query
 returns a dictionary where the key is the bird and the value is the count at that location
    '''
    return {}

#=============================================================================
# Test code below DO NOT MODIFY
BIRDS = ["Finch", "Robin", "Hummingbird", "Crow", "Eagle", "Hawk", "Cardinal", "Vulture", "Phoenix", "Sparrow"]
LOCATIONS = ["Park", "Backyard", "Skyscraper", "Forest", "Jungle", "Roadside", "Cage", "Sky", "Desert"]
TIME_OF_DAY = ["6-10AM", "10AM-2PM", "2-6PM", "6-10PM", "10PM-2AM", "2-6AM"]

birdCount    = [0] * len(BIRDS)
TEST_INDEX   = 3 # Just one selected location, no specific choice
locationTest = {}

def generateSighting():
    birdIndex = random.randrange(len(BIRDS))
    birdCount[birdIndex] = birdCount[birdIndex] + 1

    locationIndex = random.randrange(len(LOCATIONS))
    if locationIndex == TEST_INDEX: 
        if BIRDS[birdIndex] in locationTest:
            locationTest[BIRDS[birdIndex]] = locationTest[BIRDS[birdIndex]] + 1
        else:
            locationTest[BIRDS[birdIndex]] = 1
            
    return BIRDS[birdIndex], \
            LOCATIONS[locationIndex], \
            TIME_OF_DAY[random.randrange(len(TIME_OF_DAY))]

def testLedger():
    ledger = {}

    dayCount = []
    numberOfDays = random.randint(10, 20)
    if debug: print("The test cases will generate", numberOfDays, "days")
    for day in range(numberOfDays):
        numberOfSightings = random.randint(10, 50)
        dayCount.append(numberOfSightings)
        dayName = "Day " + str(day + 1)
        if debug: print(dayName, "will contain", numberOfSightings, "sightings")
        for count in range(numberOfSightings):
            sighting = generateSighting()
            addBirdSighting(dayName, sighting, ledger)

    counts = birdsSeenEachDay(ledger)
    if counts != dayCount:
        print("birdsSeenEachDay() Failed:  Your code returned", counts, "but I expected", dayCount)
    else:
        print("birdsSeenEachDay() Passed!")

    return ledger

def testNumberOfSightingsFor(ledger):
    success = True
    for index, bird in enumerate(BIRDS):
        actual = numberOfSightingsFor(bird, ledger)
        if actual != birdCount[index]:
            success = False
            print("testNumberOfSightingsFor() Failed: Your code reported", actual, "but I expected", birdCount[index], "for", bird)

    actual = numberOfSightingsFor("Ostrich", ledger)
    if actual != 0:
        print("testNumberOfSightingsFor() Failed: Your code reported", actual, "but I expected 0 for Ostrich")
    return success

def testAllBirdsSpottedAt(ledger):
    success = True
    locationDetails = allBirdsSpottedAt(LOCATIONS[TEST_INDEX], ledger)
    if locationDetails != locationTest:
        success = False
        print("testAllBirdsSpottedAt Failed!:  Your code reported", locationDetails, "but I expected", locationTest, "at", LOCATIONS[TEST_INDEX])

    actual = allBirdsSpottedAt("My House", ledger)
    if len(actual) != 0:
        success = False
        print("testAllBirdsSpottedAt Failed!:  Your code reported", actual, "but I expected no sightings at the empty value of My House")
    return success

# Only run this code below if this is called as the main, not imported
if __name__ == '__main__':
    ledger = testLedger()
    if testNumberOfSightingsFor(ledger):
        print("numberOfSightingsFor() Passed!")

    if testAllBirdsSpottedAt(ledger):
        print("testAllBirdsSpottedAt() Passed!")
