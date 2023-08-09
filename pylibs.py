
def playPylibs():
    '''
Play a game of Pylibs by asking the user for inputs and showing the resulting story
    '''
    print("Welcome to Pylibs")

    titleNumber = input("Give me a number ") # Replace this with something more interesting
    # You need at least 10 inputs total

    titleNoun = input("Give me an occupation ")

    verb1 = input("Give me  a verb ending in ing ")

    place1 = input("Give me a place ")

    place2 = input("Give me another place ")

    color = input("Give me a color ")

    fake = input("Make up a word ")

    name = input("Give me a name ")

    adj = input("Give me an adjective ending in 'est' ")

    verb2 = input("Give me a verb in past tense ")

    noun3 = input("Give me another noun ")

    verb3 = input("Give me another verb ")

    adj2 = input("Give me another adjective ")

    verb4 = input("Give me a final verb ")

    adj3 = input("Give me a final adj ")

    

    

    print("The story of", titleNumber, titleNoun)
    print("A group of", titleNumber, titleNoun, "were", verb1, "in", place1, ". They were headed towards", place2, ". They were hoping to find a", color, fake, "there.", name, "the", adj, "of the", titleNoun, verb2, noun3, ". ", name, "knew at once they had to", verb3, "the other", titleNoun, ". But before they did, the", titleNoun, "were all", adj2, ". ", name, "had to continue the search on their own. When they found the", color, fake, ", it", verb4, ". ", name, "was", adj3, ". The End")

    # Write your own story
    # You can print as many lines as you wish.  Remember each print commands
    # prints one line by default.  You can look up how to change that now if you need
    # or you will find out more later.

#=============================================================
# Testing code below - DO NOT EDIT
# Only run this code below if this is called as the main, not imported
if __name__ == '__main__':
    playPylibs()
