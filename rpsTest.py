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
    if randint == 0:
        return ROCK
    if randint == 1:
        return PAPER
    if randint == 2:
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
        if move == "rock":
            return ROCK
        if move == "paper":
            return PAPER
        if move == "scissors":
            return SCISSSORS
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
    if player1Move == player2Move:
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
        
        reportResult = RESULT_TIE # or RESULT_P1 or RESULT_P2
        #....................
        #    Add logic here to report the result and add to the the totals
        #....................
        if winner == 0:
            tieCount += 1
        if winner == 1:
            player1WinCount += 1
        if winner == 2:
            player2WinCount += 1
        
        print(reportResult)
        print("Scoreboard")
        print("---------------------")
        print("Player 1:", player1WinCount, "to Player 2:", player2WinCount, "and", tieCount, "ties")
        stop = input("Keep Playing? ").lower()
        if stop == 'no' or stop == 'n':
            return

getComputerMove()
getPlayerMove()
winner()
playGameWithUser()
#==================================================================
# Everything below here is tester code DO NOT MODIFY
#
#               R   P   S - Player 2
