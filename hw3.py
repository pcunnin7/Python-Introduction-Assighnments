#I worked on this alone

#PROBLEM 1
class Trip(object):

    def __init__(self,name='',date='',miles=0,costPerMile=0):
        '''Initialize the Trip object.  Note: only way to set values on the object
        is by using the constructor. Note.miles and costPerMiles are floats '''
        '''the contructor takes the parameters name, date, miles, and costPerMile and assigns
    them to the variables to self.n, self.d, self.m, and self.costpm per mile. '''
        self.n = name
        self.d = date
        self.m = float(miles)
        self.costpm = float(costPerMile)
        

    def getName(self):
        'get the trip name'
        'returns the self.n variable when the method is call'
        return self.n

    def getDate(self):
        'get the date of the trip'
        'returns the self.d variable when the method is call'
        return self.d

    def getMiles(self):
        'get the total miles of the trip'
        'returns the self.m variable when the method is call'
        return self.m

    def getCostPerMile(self):
        'get the cost per mile'
        'returns the self.costpm variable when the method is call'
        return self.costpm


    def calculateTotal(self):
        'calculcate the trip total'
        '''multiplies the self.costpm variable by the self.m variableand then sets the product to total,
        then returns total'''
        total = self.costpm * self.m
        return total

    def __str__(self):
        'str representation.'
        'returns a string with all the variables of the trip divided by colons'
        return(self.n + ':' + self.d + ':' + str(self.m) + ':' + str(self.costpm))

        
    def __repr__(self):
        'python representation'
        "returns the string Trip('{}','{}','{}','{}') formatted with the self.n, self.d, self.m, and self.costpm"
        return "Trip('{}','{}','{}','{}')".format(self.n, self.d, self.m,self.costpm)
    
#PROBLEM 2 and 3:
    '''
    Do not use files for the methods in trip manager, use list, and then use the list to make the files in prob. 3
'''
class TripManager(object):

    #START OF PROBLEM 2
    def __init__(self, filename='trip.txt'):
        'Initialize the TripManager class'
        '''The constructor takes the parameter filename and sets it equal to the
        variable self.file. It also creates the empty list self.trips
        '''
        self.trips = []
        self.file = filename
        
        

    def addTrip(self,trip):
        'adds an Trip to the manager'
        '''tries appending the parameter list to self.trips and returns true if successful,
        and prints 'Unable to add trip' and returns false in unsuccessful.'''
        try:
            self.trips.append(trip)
            return True
        except:
            print('Unable to add trip.')
            return False
            
        
    
    def getTripsTotal(self):
        'returns the total cost of all the trips managed.'
        '''Creates the variable tripsTotal and sets it to 0, then iterates through the self.trips list
        using a for each entry and setting b equal to the total cost of each entry.
        It then adds b to tripsTotal, and after iterating through the list returns
        tripsTotal'''
        tripsTotal = 0
        for a in self.trips:
            b = a.calculateTotal()
            tripsTotal += b
        return tripsTotal
        

    def getCountOfTrips(self):
        'returns a count of how many trips were taken'
        '''Creates the variable count and sets it to 0, then iterates through the list
        self.trips, and for each entry increases the count by one. After iterating
        through the list, it returns the count.'''
        count = 0
        for a in self.trips:
            count += 1
        return count
        

    def getAverageCost(self):
        'returns the average cost of the trips. Returns 0 if there are no trips'
        '''runs the getCountOfTrips method and checks if it is greater than 0, and
         if it is, it calculates the the average (avg) by running the getTripsTotal and dividing the
         results by the result of the getCountOfTrips. If the count is 0, then it sets avg to 0. It
         then returns avg.'''
        if self.getCountOfTrips() > 0:
            avg = avg = self.getTripsTotal() / self.getCountOfTrips()
        if self.getCountOfTrips() == 0:
            avg = 0
        return avg
        

    def getAllTripDates(self):
        'gets a list of the dates of all the trips. if there are no trips the list should be empty'
        '''creates the variable allDates and sets it equal to 0. It then iterates through the list
        self.trips and sets the entry to a, then sets b equal to result of getDate(), then appends b
        to allDates. After iterating, returns allDates
        '''
        allDates = []
        for a in self.trips:
            b = a.getDate()
            allDates.append(b)
        return allDates

    def getMostExpensiveTrip(self):
        'gets the trip with the highest total. Returns None if there are no trips.'
        '''runs the method getCountOfTrips and checks if it is greater than 0. If it is,
        then it creates the empty dictionary costs, then iterates through the self.trips
        list and sets the variable cost equal to the result of the method calculateTotal
        of the entry. It then sets the dictionary value of the key of the entry to the cost.
        After iterating through the list, it creates a list of the sortd values from the dictionary.
        It then iterates through the dictionary keys, and then checks if the value for the key is equal
        to the highest value in the sorted list. If it is, the variable highest is set to the key, and
        highest is returned. If getCountOfTrips equals 0, the method returns None'''
        if self.getCountOfTrips() > 0:
            costs = {}
            for a in self.trips:
                cost = a.calculateTotal()
                costs[a] = cost
            sort = sorted(costs.values())
            for key in costs:
                if costs[key] == sort[-1]:
                    highest = key
            return highest
        if self.getCountOfTrips() == 0:
            return None
            

    def __iter__(self):
        'iterator'
        'Iterates through the list self.trips'
        return iter(self.trips)

    #START OF PROBLEM 3

    def loadTrips(self):
        'Read the trips information from the file. You should clear out any trips that are in the manager before you load.Returns True if successful and False if there is an error'
        '''The method tries opening the file using the variable self.file, which is equal to the parameter entered when TripManager was constructed. It clears the self.trips list, then
        opens the file to read it, then iterates through the file and for each line (which is each trip) it creates a Trip and then appends the Trip to self.trips. If succesful, it
        returns true. If not, it print 'Unable to read file' and returns false'''
        try:
            self.trips.clear()
            file = open(self.file, 'r')
            for line in file:
                splits = line.strip().split(':')
                trip = Trip(splits[0],splits[1],splits[2],splits[3])
                self.trips.append(trip)
            return True
        except:
            print('Unable to read file.')
            return False
        
    def saveTrips(self):
        'write all trips to the file overwriting the existing file. Returns True if successful and False if there is an error'
        '''The method tries opening the file to write to using the variable self.file, which is equal to the parameter entered when TripManager was constructed.
        It then iterates through self.trips and for each trip it writes the trip to the file. If succesful, it returns true and closes the file. If not, it print
        'Unable to write file' and returns false'''
        try:
            file = open(self.file, 'w')
            for trip in self.trips:
                 file.write('{}\n'.format(trip))
            return True
            file.close()
        
        except:
            print('Unable to write files.')
            return False


    
