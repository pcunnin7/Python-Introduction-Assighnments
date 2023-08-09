def createHoursLog(weeks):
    '''
Creates a list structure to store the hours log, intialized to zero
   weeks - the number of weeks the log should span
 returns the initalalized list
    '''
    log = [[0 for days in range(7)] for week in range(weeks)]
    return log

def logTime(week, day, hours, log):
    '''
Update the entry for the given week and day with the provided hours
   week - the week of the course between 1 and weeks
   day - the day of the week between 1 (Sunday) and 7 (Saturday)
   hours - the number of hours to set on that day
    '''
    log[week -1][day - 1] = hours

def totalTimeForWeek(week, log):
    '''
Compute the hours spent on the provided week
   week - the selected week between 1 and weeks
   log - the log to query
 returns the total for that week
    '''
    sum = 0
    for entry in log[week - 1]:
        sum += entry
    
    return sum

def totalTimeForWeeks(start, end, log):
    '''
Compute the hours spent starting on start week and through end week provided
   start - the first week to log 1 and weeks - 1
   end - the last week to log between 2 and weeks
   log - the log to query
 returns the total for that span
    '''
    sum = 0
    for week in log[start:end+1]:
        for entry in week:
            sum += entry
    return sum

def totalTimeOnWeekends(log):
    '''
Compute the amount of time spent on weekends by the student through the entire course
   log - the log to evaluate
 returns the sum of all weekend work
 (Hint: remember that the week starts on Sunday and ends on Saturday)
    '''
    sum = 0
    for week in log:
        count = 0
        for entry in week:
            count+= 1
            if count == 1 or count == 7:
                sum += entry
    return sum

#==============================================================
# Everything below here is testing DO NOT MODIFY
def validateInitialLog(log, weeks):
    '''
Check that the initial list is correct
    '''
    if len(log) != weeks:
        print("createHoursLog() Failed: Your log has", len(log), "rows but we expected", weeks)
        return False

    for weekIndex, week in enumerate(log):
        if len(week) != 7:
            print("createHoursLog() Failed: Your log at week", weekIndex, "has", len(week), "entries but we expected 7")
            return False
        for dayIndex, entry in enumerate(week):
            if entry != 0:
                print("createHoursLog() Failed: Your log at week", weekIndex, "and day", dayIndex, "has a value of", entry, "but we expected 0")
                return False
    print("createHoursLog() Passed!")
    return True

def testLogTime(log):
    logTime(1, 5, 3, log)
    actual = log[0][4]
    if actual != 3:
        print("logTime() Failed: The week", 1, "and day", 5, "was set to", 3, "but instead was", actual)
        return False
    
    for weekIndex in range(2, 9):
        logTime(weekIndex, 2, 1.5, log)
        actual = log[weekIndex - 1][1]
        if actual != 1.5:
            print("logTime() Failed: The week", weekIndex, "and day", 2, "was set to", 1.5, "but instead was", actual)
            return False

        logTime(weekIndex, 5, 3, log)
        actual = log[weekIndex - 1][4]
        if actual != 3:
            print("logTime() Failed: The week", weekIndex, "and day", 5, "was set to", 3, "but instead was", actual)
            return False
    print("logTime() Passed!")
    return True

def testTotalWeek(log):    
    actual = totalTimeForWeek(1, log)
    if actual != 3:
        print("totalTimeForWeek() Failed: Your week", 1, "reported", actual, "but should be", 3)
        return False
    print("totalTimeForWeek() Passed!")
    return True

def testTotalWeeks(log):    
    actual = totalTimeForWeeks(2, 5, log)
    if actual != 18:
        print("totalTimeForWeeks() Failed: Your total including start", 2, "and end", 5, "reported", actual, "but should be", 18)
        return False
    print("totalTimeForWeeks() Passed!")
    return True

def testWeekends(log):
    for weekIndex in range(2, 9):
        logTime(weekIndex, 1, 3, log)

    actual = totalTimeOnWeekends(log)
    if actual != 21:
        print("totalTimeOnWeekends() Failed: Your total was", actual, "but should be", 21)
        return False
    print("totalTimeOnWeekends() Passed!")
    return True
        
# Only run this code below if this is called as the main, not imported
if __name__ == '__main__':
    log = createHoursLog(10)
    if validateInitialLog(log, 10):
        if testLogTime(log):
            if testTotalWeek(log):
               if testTotalWeeks(log):
                   if testWeekends(log):
                       print("All tests passed!")
