import random
DAYS_PER_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def generateRainfallCalendar():
    '''
Create a list to hold rainfall totals for every day in a non-leap year intialized to zero
    '''
    
    calendar = [[0 for days in range(DAYS_PER_MONTH[month])]for month in range(12)]
    return calendar

def setRainfall(month, day, amount, calendar):
    '''
Set the rainfall total for the given day
   month - the month to set, which must be between 1 and 12 or the function will return
           without adding a value
   day - the day of the month to set, which must be betwen 1 and the last day specified
         in DAYS_PER_MONTH or the function will return without adding a value
   amount - the amount of rainfall to set
   calendar - the calendar to update
    '''
    calendar[month - 1][day - 1] = amount


def getTotalForMonth(month, calendar):
    '''
Compute the total rainfall for the given month
   month - the selected month
   calendar - within this calendar
 returns the total rainfall as a floating point number
    '''
    sum = 0
    for dayRainfall in calendar[month - 1]:
        sum += dayRainfall
        
    return sum

#====================================================
# Test code below DO NOT MODIFY

def testCalendar():
    calendar = generateRainfallCalendar()
    monthlyTotals = []
    success = True

    for month in range(12):
        sumForMonth = 0
        for day in range(random.randint(5, DAYS_PER_MONTH[month]//2)):
            amount = random.uniform(0, 3)
            sumForMonth = sumForMonth + amount
            setRainfall(month + 1, day + 1, amount, calendar)
        monthlyTotals.append(sumForMonth)

    for month, total in enumerate(monthlyTotals):
        actual = getTotalForMonth(month + 1, calendar)
        if actual != total:
            success = False
            print("Failure: I expected that month", month, "should be", total, "but your code returned", actual)
            
    if success:
        print("Your Rainfall Calendar Passed!")

# Only run this code below if this is called as the main, not imported
if __name__ == '__main__':
    testCalendar()
