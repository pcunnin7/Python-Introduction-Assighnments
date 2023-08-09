def canadian(quote):
    out = ''
    out = quote + ", eh?"
    return out 

def shatner(quote):
    out = ''
    tokens = quote.split(" ")
    for token in tokens:
            out = out + token + "...\n"
    return out

def valleyGirl(quote):
    out = ''
    tokens = quote.split(" ")
    for count, token in enumerate(tokens):
            out = out + "like ";
            out = out + token;
            if count < len(tokens) - 1:
                out = out + " ";
    return out 

def pirate(quote):
    out = ''
    tokens = quote.split(" ")
    for count, token in enumerate(tokens):
        for char in token:
            if char == 'r' or char == 'R':
                out = out + "RRR";
            out = out + char
        if count < len(tokens) - 1:
            out = out + " ";
    return out

def zatanna(quote):
    out = ''
    tokens = quote.split(" ")
    for count, token in enumerate(tokens):
            out = out + token[::-1];
            if count < len(tokens) - 1:
                out = out + " ";
    return out

def yoda(quote):
    out = ''
    tokens = quote.split(" ")
    write = False
    save = ""
    for count, token in enumerate(tokens):
        if (write):
            write = False
            out = out + token + " " + save
            if count < len(tokens) - 1:
                out = out + " ";
        else:
            write = True
            save = token
    if write:
        out = out + save + "\n";
    return out

def generateQuote(quote, accentName):
    '''
Transform the quote to a script for the accent provided
   quote - the quote to change
   accentName - the name of the accent to generate
 return the modified quote
    '''
    #sets out to empty string so that the different outputs can be added to out later
    #splits the quote into all of its words, so that each word can be worked with individually
    if accentName =="Canadian":
        out = canadian(quote)
    elif accentName =="Shatner":
        out = shatner(quote)
            #checks if accent is Shatner, if it is then for each word it adds the word and a new line to out to break up the quote like Shatner
    elif accentName =="Valley Girl":
        out = valleyGirl(quote)
                #checks if accent is valley girl, if it is then for each word adds 'like' and then the word. Then adds space between the last word and next like to imitate the valley girl accent
    elif accentName =="Pirate":
        out = pirate(quote)
                #checks if accent is pirate, if it is then searches for the letter r and adds RRR before to make it sound like the typical pirate. Then adds a space between each word)
    elif accentName =="Zatanna":
        out = zatanna(quote)
                #checks  if accent is Zatanna, if it is then adds each word backwards to out. Adds a space at the end of each word. Effectively makes each word said backwards without flipping the whole quote 
    elif accentName =="Yoda":
        out = yoda(quote)
            #checks  if accent is Yoda, if it is then switches each word with one next to it to replicate Yoda's speech
        
    return out
    
TESTS = [["Canadian", "Four score and seven years ago, eh?"],
         ["Valley Girl", "like Four like score like and like seven like years like ago"],
         ["Shatner", "Four...\nscore...\nand...\nseven...\nyears...\nago...\n"],
         ["Pirate", "FouRRRr scoRRRre and seven yeaRRRrs ago"],
         ["Zatanna", "ruoF erocs dna neves sraey oga"],
         ["Yoda", "score Four seven and ago years"]]
    
def main():
    quote = "Four score and seven years ago"
    print("Original Quote: \"" + quote + "\"");
    for test in TESTS:
        print(".....................................")
        print("Testing ", test[0], ":")
        answer = generateQuote(quote, test[0])
        if answer == test[1]:
            print("Success")
        else:
            print("Your code returned the quote:...")
            print(answer)
            print("but I expected: ")
            print(test[1])
main()
