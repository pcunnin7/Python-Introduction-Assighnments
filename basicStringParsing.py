#a Splitting a String (& Substrings)
def countLettersInName(nameString):
    count = 0
    splits = nameString.split("\n")
    for split in splits:
        colon = split.find(":")
        for charactor in split[colon + 1:]:
            count+= 1
    return count
    '''
A fortune teller needs to quickly compute the number of letters in a person's name
to foresee their future.  They have an app that produces a string such as
 "First:Anthony\nMiddle:Andrew\nLast:Lowe"
The count should be the number of characters in the first, middle, and last names,
not including the labels.  A person may not have a first, middle, and/or last name.
A person may include any character in their name (spaces too) and they count.
   nameString - the full name to parse
 returns the integer count of characters in their name
    '''

#b Splitting and Finding
def evaluatePingReport(report):
    count = 0
    pingAverage     = 0
    numberOfTimeouts = 0
    total = 0
    lines = report.split("\n")
    for line in lines:
        if line.find("Request Timed out") == -1:
            ms = line.find("ms")
            time = line.find("time=")
            ping = line[time+5:ms]
            if ping >= "0":
                count += 1
                total += int(ping)
           
        
        else:
            numberOfTimeouts += 1
    pingAverage = (total / (count) )
            
    return (pingAverage, numberOfTimeouts)

'''
A windows computer can track the speed of your internet by 'pinging' another server.
A report of such a command might look like the following:
    Reply from 216.58.192.206: bytes=32 time=30ms TTL=115\n
    Reply from 216.58.192.206: bytes=32 time=28ms TTL=115\n
    Request Timed out.\n
A successful ping reports the time of the ping of
  time=30ms
  time=28ms
where a failed ping says it
  Request Timed out.

This procedure computes the average of the ping times and the number of timeouts
from the provided report.
   report - a string where each \n represents a new line on the report
 returns the tuple (<ping average>, <numberOfTimeouts>)
    '''
    # Keep these variables and fill them to return at the end

    # You must return exactly these variables (defined above) after you compute
    # and assign them values

#c Multi-level Parsing
def computeCurrentGradePercentage(gradeReport):
    pointsEarned = 0
    totalPoints = 0
    splits = gradeReport.split(",")
    for split in splits:
        colon = split.split(":")
        for entry in colon[1:]:
            numbers = entry.split("/")
            pointsEarned += float(numbers[0])
            totalPoints += float(numbers[1])
    score = (pointsEarned / totalPoints)
                
            
            
    '''
A teacher uses one grading system to track individual  grades but must report the
final grades to a different  system as a percentage.  The first system only provides a
report in text for the grades, so you must parse that report. For example,
 A report of "Essay:9/10" should return 0.9
 A report of "Project:22.5/25, Test:82/100" should return 0.836
Create logic to parse any number of assignments (separated by commas) and parse their
scores (after the :, earned then a slash (/) then the possible score) to compute the final
grade percentage (earned/possible)
   gradeReport - the text report to parse
 returns a numerical percentage value (likely between 0-1 but could exceed 1)
    '''
    return score
        
#==========================================================
# DO NOT MODIFY anything below here, test code
def testCount():
    '''
Test the countLettersInName() function
    '''
    TEST = {"First:Anthony\nMiddle:Andrew\nLast:Lowe": 17,
            "First:Albus\nMiddle:Percival Brian Wolfrick\nLast:Dumbledore": 38,
            "First:Jane\nMiddle:\nLast:Doe": 7,
            "First:Bono\nMiddle:\nLast:": 4}
    success = True
    for test in TEST:
        result = countLettersInName(test)
        if result != TEST[test]:
            success = False
            print("Failed countLettersInName():  For the name (" + test +
                  "), your code returned", result, "but the expected answer is", TEST[test])
    if success:
        print("Passed countLettersInName()")
    return success

def testPing():
    '''
Test the evaluatePingReport() function
    '''
    TEST = '''
        Reply from 216.58.192.206: bytes=32 time=30ms TTL=115\n
        Reply from 216.58.192.206: bytes=32 time=30ms TTL=115\n
        Reply from 216.58.192.206: bytes=32 time=28ms TTL=115\n
        Request Timed out.\n
        Reply from 216.58.192.206: bytes=32 time=29ms TTL=115\n
        Reply from 216.58.192.206: bytes=32 time=29ms TTL=115\n
        Reply from 216.58.192.206: bytes=32 time=28ms TTL=115\n
        Reply from 216.58.192.206: bytes=32 time=28ms TTL=115\n
        Reply from 216.58.192.206: bytes=32 time=30ms TTL=115\n
        Request Timed out.\n
        Reply from 216.58.192.206: bytes=32 time=29ms TTL=115\n
        Reply from 216.58.192.206: bytes=32 time=31ms TTL=115\n
        '''

    results = evaluatePingReport(TEST)
    if results[0] != 29.2:
        print("Failed evaluatePingReport(): you returned an average of", results[0],
              "but the expected value was 29.2")
    elif results[1] != 2:
        print("Failed evaluatePingReport(): you returned a failed ping count of", results[1],
              "but the expected value was 2")
    else:
        print("Passed evaluatePingReport()")
        return True
    return False

def testGrades():
    '''
Test the computeCurrentGradePercentage() function
    '''
    TEST = {"Essay:9/10": 0.9,
            "Project:22.5/25, Test:82/100": 0.836,
            "Test 1:85/100, Test 2:45/52, Test 3:25/31": 0.8469945355191257,
            "Homework:110/100, Quizzes:100/100, Tests:60/60": 1.0384615384615385}
    success = True
    for test in TEST:
        result = computeCurrentGradePercentage(test)
        if result != TEST[test]:
            success = False
            print("Failed computeCurrentGradePercentage():  For the input (" + test +
                  "), your code returned", result, "but the expected answer is", TEST[test])
    if success:
        print("Passed computeCurrentGradePercentage()")
    return success

if __name__ == '__main__':
    success = True
    success = testCount() and success
    success = testGrades() and success
    success = testPing() and success
    if success:
        print("All tests Passed!")
