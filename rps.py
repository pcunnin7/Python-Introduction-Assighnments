from random import randint

# 'constant's to define the three moves
NUMBER_OF_POSSIBLE_MOVES = 3
ROCK     = "rock"
PAPER    = "paper"
SCISSORS = "scissors"

#........... 1 ...........................................
def getComputerMove():
    '''
A function the retrieve the computer's move
 returns one of the valid moves
    '''
    move = randint(0, NUMBER_OF_POSSIBLE_MOVES - 1)
    if move == 0:
        return ROCK
    elif move == 1:
        return PAPER
    elif move == 2:
        return SCISSORS
#........... 2 ...........................................
def getPlayerMove():
    '''
Ask the user for their move and ensure they have selected one of the
valid moves or a shortcut of your choice
 returns one of the valid moves
    '''
    while True:
        move = input("Player 1 Move: ").lower()
        if move == "rock" or move == "r":
            return ROCK
        if move == "paper" or move == "p":
            return PAPER
        if move == "scissors" or move == "s":
            return SCISSORS
        if move != "rock" or "paper" or "scissors":
            print("Please type a valid option")

        # Your code needs to decide if the input is one of the valid
        # options (e.g., You might allow any of Rock, rock, r, R, or others).
        # If the input does not match any of the options, tell the player to
        # choose one of the valid options

#........... 3 ...........................................

def winner(player1Move, player2Move):
    if player1Move == ROCK and player2Move == SCISSORS:
        return 1
    if player1Move == SCISSORS and player2Move == ROCK:
        return 2
    if player1Move == SCISSORS and player2Move == PAPER:
        return 1
    if player1Move == PAPER and player2Move == SCISSORS:
        return 2
    if player1Move == PAPER and player2Move == ROCK:
        return 1
    if player1Move == ROCK and player2Move == PAPER:
        return 2
    else:
        return 0
    
    '''
A function to determine the winner
  player1Move - one of the move constants
  player2Move - one of the move constants
 returns the winner (1 or 2) or 0 in case of a tie
    '''
    # You should implement this logic here

#........... 4 & 5...........................................
def playGameWithUser():
    '''
Prompts the user for moves to play the game
    '''
    RESULT_TIE = "-Tie-"
    RESULT_P1  = "Player 1 wins!"
    RESULT_P2  = "Player 2 wins!"
    player1WinCount = 0
    player2WinCount = 0
    tieCount = 0

    print("Welcome to Rock, Paper, Scissors")
    while True:
        playerMove   = getPlayerMove()
        print("Player 1 chose:", playerMove)
        computerMove = getComputerMove()
        print("Player 2 chose:", computerMove)
        result = winner(playerMove, computerMove)

        if result == 0:
            reportResult = RESULT_TIE
        if result == 1:
            reportResult = RESULT_P1
        if result == 2 :
            reportResult = RESULT_P2
        #....................
        #    Add logic here to report the result and add to the the totals
        #....................
        if result == 0:
            tieCount += 1
        if result == 1:
            player1WinCount += 1
        if result == 2:
            player2WinCount += 1
        
        print(reportResult)
        print("Scoreboard")
        print("---------------------")
        print("Player 1:", player1WinCount, "to Player 2:", player2WinCount, "and", tieCount, "ties")
        stop = input("Keep Playing? ").lower()
        if stop == 'no' or stop == 'n':
            return 



#==================================================================
# Everything below here is tester code DO NOT MODIFY
#
#               R   P   S - Player 2
TEST_CASES = [[ 0,  2,  1 ], #R - Player 1
              [ 1,  0,  2 ], #P
              [ 2,  1,  0 ]] #S
CROSSWALK  = { 0 : ROCK, 1 : PAPER, 2 : SCISSORS }
import subprocess


def testComputerMove():
    success = True
    moves = {ROCK : 0, PAPER : 0, SCISSORS : 0}
    for turn in range(100):
        move = getComputerMove()
        moves[move] = moves[move] + 1
    
    for move in moves:
        if moves[move] < 20:
            success = False
            print("Test case failed - testComputerMove: Your code generated", moves[move],
                  "moves for", move,
                  "but I would expect the random generator to produce more than 20")
    return success

def testWinner(player1Move, player2Move):
    answer = winner(CROSSWALK[player1Move], CROSSWALK[player2Move])
    if not answer == TEST_CASES[player1Move][player2Move]:
        print("Test case failed- Player 1:",  CROSSWALK[player1Move], "& Player 2:", CROSSWALK[player2Move],
              "- Expected:", TEST_CASES[player1Move][player2Move], "Got:", answer)
        return False
    return True

def testPlayerMove():
    success = True
    tests = [("r\n", ["Player 1 chose: rock"]),
             ("p\n", ["Player 1 chose: paper"]),
             ("s\n", ["Player 1 chose: scissors"]),]
    for inputs, expected in tests:
        uut = subprocess.Popen('python rps.py -test'.split(),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        output, err = uut.communicate(inputs.encode(), 1)
        result = str(output)
        for item in expected:
            if result.find(item) == -1:
                success = False
                print("...... Player Move Test Failed......",
                      "The automated tester sent the inputs:", inputs,
                      "and expected your code to return:", expected,
                      "but instead your code returned (the last value):", result, sep='\n')
                break
    return success

def testScoreboard():
    success = True
    tests = [("r\n", ["Player 1: 1 to Player 2: 0 and 0 ties",
                      "Player 1: 0 to Player 2: 1 and 0 ties",
                      "Player 1: 0 to Player 2: 0 and 1 ties"])]
    for inputs, expected in tests:
        uut = subprocess.Popen('python rps.py -test'.split(),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        output, err = uut.communicate(inputs.encode(), 1)
        result = str(output)
        present = False
        for item in expected:
            if result.find(item) >= 0:
                present = True
                break
        if not present:
            success = False
            print("...... Scoreboard Test Failed......",
                  "The scoreboard should have updated but did not", sep='\n')
            break
            
    return success

def tester():
    success = True
    success = success and testComputerMove()
    success = success and testPlayerMove()
    for player1Move in range(NUMBER_OF_POSSIBLE_MOVES):
        for player2Move in range(NUMBER_OF_POSSIBLE_MOVES):
            success = success and testWinner(player1Move, player2Move)
    success = success and testScoreboard()
    if success:
        print("All winner tests passed!")

import sys
if __name__ == '__main__':
    if len(sys.argv) == 1: #Ignore this for the automated tester, which adds a parameter
        tester()
    playGameWithUser()
