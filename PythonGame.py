import random
import string

catPool = ["Colors", "Foods", "Sports", "Countries", "Animals", "Plants", "Actors", "Singers", "Writers", "Movies", "Instruments", "Songs", "Books", "Board games", "Presidents", "Drinks", "Body parts"]
ans = []
catGame = []
letter = random.choice(string.ascii_uppercase)


def gameStart():
    rounds = int(input('How many rounds? '))
    players = int(input('How many players? '))
    for count in range(rounds):
        catGame.append(random.choice(catPool))
    for player in range(1, players):
        name = str(player)
        file1 = open(name + '.py', 'w')
        file2 = open('projectTester.py', 'r')
        for line in file2:
            file1.write(line)
    gamePlay(rounds)

def gamePlay(rounds):
    score = 0
    pName = input('Enter Your Name to Begin! ')
    print('The letter is: ' + letter)
    for n in range(rounds):
        print('Round ' +str(n+1) + ': ' + catGame[n])
        ans.append(input('Your Answer: '))
        if ans[n][0] == letter:
            score += 1
    print('That was the last round! ')
    print('You can score ' +score+ ' points!')
    print('Please Return This Filr To The Starting Player.')
    



gameStart()
