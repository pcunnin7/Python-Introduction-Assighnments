# Annotate this code to identify what each segment is doing.  Identify places where
#   you could split the code into multiple functions
# Using your analysis, refactor this code to simplify and make it resuable by
#   making additional functions

def search(findMe, linesOfCode):
    count = 0
    inBlockQuote = False
    for line in linesOfCode:
        #The challenges is when you have a full quote before the comment
        # so you have to check if you are in a quote before you count any character
        inQuote = False
        inComment = False
        comment = False
        for index in range(len(line)):
            if line[index] == "#":
                comment = True
            if comment == True and "#" in line[:index]:
                inComment = True
                


            # This logic is not perfect, as if you have ''''' it will get confused
            if not inQuote and not inComment and index + 3 < len(line) and line[index:index + 3] == "'''":
                inBlockQuote = not inBlockQuote
                
            # This logic is also flawed, as it does not look for ' and " strings 
            if not inBlockQuote and line[index] == "\"":
                if inQuote and line[index - 1] == "\\":
                    pass # it is a quote character literal
                else:
                    inQuote = not inQuote

            if not inQuote and not inBlockQuote and inComment == False and index + len(findMe) < len(line) and line[index:index + len(findMe)] == findMe:
                count +=  1
                print(line)
            
    return count

def makeLines(file):
    linesOfCode = []
    for line in file:
        linesOfCode.append(line)
    return linesOfCode
    

def countLines(code):
    totalLinesOfCode = len(code)
    
    return totalLinesOfCode

def countNonBlank(code):
    for line in code:
        if len(line.strip()) == 0:
            code.remove(line)
    totalNonBlankLinesOfCode = len(code)
    return totalNonBlankLinesOfCode    
    

def main():
    #lines 9-21 use this code as a file, adds each line to a list, records the number in the list
    #then removes all the blank lines. It then records the new number of lines as the total non blank
    #lines and the difference between the total lines and the non blank lines as the blank lines
    file = open("refactorUsefulFunctions.py", 'r')
    linesOfCode = makeLines(file)
    totalLinesOfCode = countLines(linesOfCode)
    totalNonBlankLinesOfCode = countNonBlank(linesOfCode)
    
    totalBlankLines = totalLinesOfCode - totalNonBlankLinesOfCode;

    '''
      Avoid picking up # in block comments too
    '''
    #lines 28-56 search for # symbols in order to find comments and makes sure the
    #symbols are not in comments/quotes, then records the number of comments
    REALLY_TRICKY_TEST = "\"#"
    totalComments = search("#", linesOfCode)
    

    #using the same method as the last section, lines 59-86 look for def, checks if it is
    #in a comment/quote, and then counts it if it is not to count the number of functions
    numberOfFunctions = search("def", linesOfCode)
    
    print("This code has a total of", totalLinesOfCode, "of which", totalBlankLines, \
          "were blank and", totalNonBlankLinesOfCode, "had content")

    print("The author included", numberOfFunctions, "functions and", totalComments, "comments")
main()
