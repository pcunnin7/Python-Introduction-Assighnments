import random

#............. 1 .............................
def readSpellingWords(filename):
    words = []
    file = open(filename,'r')
    for line in file:
        word = line[:-1]
        words.append(word)
    '''
Load the spelling words from the provided file into a list.
Each line in the file contains a single spelling word
   filename - the file to load from
 returns a list of the words in the file
    '''
    return words

#............. 2 .............................
def saveAttempt(attempt, targetWord, attemptedWord, filename):
    file = open(filename, 'w')
    file.write(str(attempt))
    file.write(targetWord)
    file.write(attemptedWord)
    print(file)
        
    '''
Save a students's attempt to the provided file.  The data should appear in
file as its own line using the provided format:
<attempt>, <targetWord>, <attemptedWord>

For example;
1, cat, kat
2, cat, cat
...
   attempt - an integer representing the attempt number overall
   targetWord - the correct spelling of the word
   attemptedWord - the student's attempt
   filename, the name of the target file for the results
    '''
    #Implement Me

#............. 3 .............................
def loadResults(filename):
    '''
Load the test data from the provided file (the one you produced in saveAttempt above)
   filename - the name of the file to load
 returns a list of 'tuples' (attempt number, target word, attempted word)
    '''
    results = []

    #You must create a tuple for each row in the file using the following
    
    # These three variables are an example of creatomg a tuple and adding
    # the tuple to a list...
    attempt       = 0  
    targetWord    = "" 
    attemptedWord = "" 
    results.append((attempt, targetWord, attemptedWord))
    
    return results
        
#............. 4 .............................
def analyzeAttempts(results):
    '''
Process the statistics for the provided student results
    '''
    #=================================================
    #Fill these variables below by processing information from the file
    totalAttempts = 0
    missedAttempts = 0
    numberOfWords = 0
    #Do not change the variables above
    #=================================================

    # Fill the variables above with your logic here
    # The statement below returns your answer

    #=================================================
    # Do not modify this return statement.
    return (totalAttempts, missedAttempts, numberOfWords)
    # Do not modify this return statement.
    #=================================================

#===========================================================
# DO NOT MODIFY anything below here, unit test code
SPELLING_WORDS_FILENAME = "spellingWord.txt"
SPELLING_RESULTS_FILENAME = "spellingWordResults.txt"
SPELLING_WORDS = ["pedagogy", "iconic", "prospection", "curmudgeon", "keratotomy"]

def setupSpellingWordsFiles():
    '''
Create/recreate the spelling word file for clean testing each time
and clear the results file
    '''
    file = open(SPELLING_WORDS_FILENAME, "w")
    for word in SPELLING_WORDS:
        file.write(word)
        file.write("\n")
    file.close
    
    file = open(SPELLING_RESULTS_FILENAME, "w")
    file.close

def checkWords(words):
    '''
Check if the loaded spelling words match the originals
    '''
    if words != SPELLING_WORDS:
        print("Failure in readSpellingWords: Your loaded words\n", words,
              "\ndid not match the test words\n", SPELLING_WORDS)
    else:
        print("Passed readSpellingWords()")

ledger = {}
def makeAttempts():
    '''
Randomly setup attempts at the test for the saveAttempt function to save
    '''
    count = 0
    for word in SPELLING_WORDS:
        trying = True
        attempts = []
        while trying:
            variation = random.randint(0, len(word)*2)
            if variation < len(word):
                submittedWord = word[:variation] + \
                                chr(ord(word[variation]) + 1) + \
                                word[variation + 1:]
            else:
                submittedWord = word
                trying = False

            attempts.append(submittedWord)
            saveAttempt(count, word, submittedWord, SPELLING_RESULTS_FILENAME)
            count = count + 1
        ledger[word] = attempts;
    return count

def checkResults(results, count):
    '''
Check the results list from loading the results
    '''
    success = True

    if len(results) != count:
        success = False
        print("Failure in loadResults: your code returned", len(results),
              "entries, but should have returned", count, "entries")
    else:
        overallCount = 0
        for entry in ledger:
            for attempt in ledger[entry]:
                result = results[overallCount]
                if type(result[0]) != int:
                    print("Failure in loadResults: expected the count to be an integer but your code provided a ", type(result[0]))
                elif result[0] != overallCount or \
                   result[1] != entry or \
                   result[2] != attempt:
                    success = False
                    print("Failure in loadResults: expected (", overallCount, ",", entry, ",", attempt,")",
                          "got (", result[0], ",",result[1], ",",result[2], ")") 
                overallCount = overallCount + 1
    if success:
        print("Passed loadResults")

def checkAnalysis(analysis, count):
    success = True
    
    if analysis[0] != count:
        success = False
        print("Failed analyzeAttempts (totalAttempts): you returned", analysis[0],
              "but there were", count, "total attempted words")

    missed = count - len(SPELLING_WORDS)
    if analysis[1] != missed:
        success = False
        print("Failed analyzeAttempts (missedAttempts): you returned", analysis[1],
              "but there were", missed, "missed words")

    if analysis[2] != len(SPELLING_WORDS):
        success = False
        print("Failed analyzeAttempts (numberOfWords): you returned", analysis[2],
              "but there were", len(SPELLING_WORDS), "words")
        
    if success:
        print("Passed analyzeAttempts()")

def mainProcess():
    setupSpellingWordsFiles()
    words = readSpellingWords(SPELLING_WORDS_FILENAME)
    checkWords(words)
    count = makeAttempts()
    results = loadResults(SPELLING_RESULTS_FILENAME)
    checkResults(results, count)
    analysis = analyzeAttempts(results)
    checkAnalysis(analysis, count)
    
if __name__ == '__main__':
    mainProcess()
