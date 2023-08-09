# DO NOT MODIFY this early part.........
class COVIDData:
    '''
A class to hold the data loaded from the file.
This is a preview of something you will learn more about later.
For now know that you can access any of the data items in here using the 'dot' notation
For example if you have a value named data then you could write a statement like...
    if data.year == 2020:
to check if the year in that data item is 2020
    '''
    def __init__(self, day, month, year, cases, deaths, country, population, continent):
        self.day   = day
        self.month = month
        self.year  = year
        self.cases = cases
        self.deaths     = deaths
        self.country    = country
        self.population = population
        self.continent  = continent

    def __str__(self):
        return str(self.day) + "/" + str(self.month) + "/" + str(self.year) + " - " + \
               self.country + ", " + self.continent + ": " + str(self.cases) + ", " + \
               str(self.deaths) + ", " + str(self.population)

    def __eq__(self, other):
        return self.day == other.day and self.month == other.month and self.year == other.year and \
               self.cases == other.cases and self.deaths == other.deaths and \
               self.country == other.country and self.population == other.population and self.continent == other.continent
# DO NOT MODIFY above here.........

populationPerCountry = {}
casesPerContinent = {}
countriesPerContinent = {}

#....................... 1 ......................................
def readDataFile(filename):
    '''
Load the COVID data from the file and create objects for each entry
   filename - the file to load from
 returns a list COVIDData objects
    '''
    # Replace this with your working solution from the Files exercise!
    entries = []
    return entries

#....................... 2 ......................................
def createReportFile(data, country, filename):
    '''
Create a report file for the provided country.  The file should contain just the saved values from the
provided list of data in the following format:
<country>, <continent>, <population>, <day>, <month>, <year>, <cases>, <deaths>
   data - a list of the entire data set
   country - the name of the country to report
   filename - the name of the file into which the report is saved
    '''
    # Replace this with your working solution from the Files exercise!

#....................... 3 ......................................
def getCasesByContinent():
    '''
From the loaded data, return the total reported cases on each continent
 returns a dictionary where the key is the continents and the value is the number of cases in that continent
    '''
    return {}

#....................... 4 ......................................
def getCountriesByContinent():
    '''
From the loaded data, return the countries on each continent
 returns a dictionary where the key is the continents and the values are a list of countries on that continent
    '''
    return {}

#....................... 5 ......................................
def getPopulationByContinent():
    '''
From the loaded data, return the total population on each continent
 returns a dictionary where the key is the continents and the value is the population of that continent
    '''
    populationPerContinent = {}
    return populationPerContinent

#============================================================
# Test code below DO NOT MODIFY    
def checkLoad(data):
    '''
Validate the loaded file matches the original file with a few spot checks
    '''
    success = True
    totalCount = 46580
    if len(data) != totalCount:
        success = False
        print("Error in readDataFile: your code loaded", len(data), "records, but the full count is", totalCount)

    first = COVIDData(3, 10, 2020, 5, 0, "Afghanistan", 38041757, "Asia")
    if data[0] != first:
        success = False
        print("Error in readDataFile: your code loaded the first entry as", data[0], ", but the desired data is", first)

    last = COVIDData(21, 3, 2020, 1, 0, "Zimbabwe", 14645473, "Africa")

    if len(data) != totalCount:
        success = False
        print("Error in readDataFile: your code loaded", len(data), "records, but the full count is", totalCount)
    elif data[totalCount - 1] != last:
        success = False
        print("Error in readDataFile: your code loaded the last entry as", data[totalCount - 1], ", but the desired data is", last)

    if success:
        print("Passed readDataFile()")

def createReportEntry(line):
    tokens = line.split(',')
    return COVIDData(int(tokens[3]), int(tokens[4]), int(tokens[5]), int(tokens[6]), int(tokens[7]), tokens[0].strip(), int(tokens[2]), tokens[1].strip())

def checkReport(data, country, filename):
    '''
Validate that the report file contains the country data
    '''
    success = True
    try:
        file = open(filename, 'r')
        for entry in data:
            if entry.country == country:
                expected = createReportEntry(file.readline())
                if expected != entry:
                    success = False
                    print("Error in createReportFile: your entry of", entry, "did not match the original of", expected)
                    break
    except FileNotFoundError:
        success = False
        print("Error in createReportFile: your file is not created yet")
    except:
        success = False
        print("Error in createReportFile: an exception occured")
        
    if success:
        print("Passed createReportFile()")

CONTINENT_CASES = {"Asia" : 10814423, "Oceania" : 33791, "America" : 17043337, "Africa" : 1498661, "Europe" : 5289291}
CONTINENT_COUNTS = {"Asia" : 43, "Oceania" : 8, "America" : 49, "Africa" : 55, "Europe" : 54}
CONTINENT_POPULATION = {"Asia" : 4542059903, "Oceania" : 40438886, "America" : 1013601796, "Africa" : 1306903030, "Europe" : 766212338}

def testPopulation():
    success = True
    actual = getPopulationByContinent()
    if type(actual) != dict or len(actual) == 0:
        success = False
        print("getPopulationByContinent() Failed: the return was not a dictionary or was empty")
    else:
        for continent in actual:
            if actual[continent] != CONTINENT_POPULATION[continent]:
                success = False
                print("getPopulationByContinent() Failed: I expected", continent, "to have a population of",
                      CONTINENT_POPULATION[continent], "but your data reported", actual[continent])
    if success:
        print("getPopulationByContinent() Passed!")

def testCases():
    success = True
    actual = getCasesByContinent()
    if type(actual) != dict or len(actual) == 0:
        success = False
        print("getCasesByContinent() Failed: the return was not a dictionary or was empty")
    else:
        for continent in actual:
            if actual[continent] != CONTINENT_CASES[continent]:
                success = False
                print("getCasesByContinent() Failed: I expected", CONTINENT_CASES[continent],
                      "cases in", continent, "but your data contiained", actual[continent])
    if success:
        print("getCasesByContinent() Passed!")


def testCountries():
    success = True
    actual = getCountriesByContinent()
    if type(actual) != dict or len(actual) == 0:
        success = False
        print("getCountriesByContinent() Failed: the return was not a dictionary or was empty")
    else:
        for continent in actual:
            if len(actual[continent]) != CONTINENT_COUNTS[continent]:
                success = False
                print("getCountriesByContinent() Failed: I expected", CONTINENT_COUNTS[continent],
                      "countries in", continent, "but your data contiained", len(actual[continent]))
    if success:
        print("getCountriesByContinent() Passed!")

FILENAME = "download.csv"
REPORT_FILENAME = "report.txt"
def mainProcess():
    data = readDataFile(FILENAME)
    checkLoad(data)
    createReportFile(data, "Belize", REPORT_FILENAME)
    checkReport(data, "Belize", REPORT_FILENAME)

    testPopulation()
    testCountries()
    testCases()

# Only run this code below if this is called as the main, not imported
if __name__ == '__main__':
    mainProcess()
