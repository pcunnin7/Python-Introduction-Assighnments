import random


TEST_INPUT_FILE_NAME = "testReadMe.txt"
TEST_OUTPUT_FILE_NAME = "testWritedMe.txt"

def readAndWrite():
    count = 0
    total = 0
    file = open("testReadMe.txt", 'r')
    for line in file:
        count+= 1 
        total += int(line)
    average = (total / count)
    
    file.close()
    file = open("testWritedMe.txt",'w')
    file.write("count: ")
    file.write(str(count))
    file.write("\n")
    file.write("total: ")
    file.write(str(total))
    file.write("\n")
    file.write("average: ")
    file.write(str(average))
    file.write("\n")
    
    '''
Reads the TEST_INPUT_FILE_NAME (which contains one number on each line) and
computes the number of numbers in the file, their total, and their average.
The process then writes these three values using the EXACT format:
count: <the count>
total: <the total>
average: <the average>
    '''
    pass




#...............................................................
# DO NOT MODIFY anything below here as it is critical to the tester
VALUE_COUNT = 100
generatedValues = []

def setupFile():
    '''
Prepare the testing input file with a new set of random numbers
    '''
    file = open(TEST_INPUT_FILE_NAME, "w")
    for count in range(random.randrange(VALUE_COUNT//2, VALUE_COUNT)):
        number = random.randint(1, 1000)
        generatedValues.append(number)
        file.write(str(number))
        file.write("\n")
    file.close()

def validateFile():
    '''
Check the file produced by the test code to see if they read/wrote correctly
    '''
    try:
        file = open(TEST_OUTPUT_FILE_NAME, "r")
    except IOError:
        print("The file named in the constant TEST_OUTPUT_FILE_NAME does not exist," +
              " create this file in your code to continue testing")
        return
    line = file.readline()
    count = int(line[7:-1])
    line = file.readline()
    total = int(line[7:-1])
    line = file.readline()
    average = float(line[9:-1])

    success = True
    if count != len(generatedValues):
        success = False
        print("Count Failed: expected", len(generatedValues),
              "your file said", count)

    sum = 0
    for value in generatedValues:
        sum = sum + value
        
    if total != sum: 
        success = False
        print("Total Failed: expected", sum,
              "your file said", total)

    avg = sum / count
    if average != avg:
        success = False
        print("Total Failed: expected", avg,
              "your file said", average)

    if success:
        print("Read and Write success!")
    else:
        print("Not yet reading and writing")


def mainTester():
    '''
Drive this exercise
    '''
    setupFile()
    readAndWrite()
    validateFile()

if __name__ == '__main__':
    mainTester()
