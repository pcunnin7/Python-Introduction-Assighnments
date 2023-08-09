debugMove = False          # Flip to True to see print statements to help in debugging makeMove()
runValidationTests = True  # Flip to True if you are completing the validGameMove() function
debugValidate = False      # Flip to True to see print statements to help in debugging validGameMove()
playAfterTest = True       # Flip to True to use the User Interface to make test moves
moveLimit = 10             # Set for the maximum number of moves in a game (Hit Control-C to quit any game)

# These are the success and error messages returned by validGameMove()
OK_MOVE         = "OK"
WRONG_PIECE     = "This space does not contain your piece"
ONLY_2          = "You can only move a piece one space diagonally, or two when legally jumping"
PLAYER_1_UP     = "Player 1 must move up"
PLAYER_2_DOWN   = "Player 2 must move down"
SPACE_TAKEN     = "The destination space is already taken"
JUMP_SELF       = "You cannot jump your own piece"
JUMP_EMPTY      = "You cannot jump an empty space"
UNKNOWN_INVALID = "Your move is not valid for an unknown reason"

#.................... 1 ........................................
def initializeBoard():
    '''
Setup the board for a new game with 2 for player 2 pieces, 1 for player 1 pieces
and 0 for blank spaces.
 returns a list with the players pieces setup for the start of a game
    '''
    board = [[0, 2, 0, 2, 0, 2, 0, 2],
             [2, 0, 2, 0, 2, 0, 2, 0],
             [0, 2, 0, 2, 0, 2, 0, 2],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 1, 0, 1, 0, 1, 0],
             [0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0]]
    return board

#.................... 2 ........................................
def makeMove(player, move, board):
    '''
Update the board with the requested move
   move - the validated move
   board - the game board
 returns the updated board
    '''
    
    jumpFindRow = int((move[1]+move[3]) / 2)
    jumpFindColumn = int((move[0]+move[2]) /2)
    board[move[1]][move[0]] = 0
    board[move[3]][move[2]] = player
    if abs((move[1] - move[3])) == 2 and abs((move[0] - move[2])) == 2 and player == 2 and board[jumpFindRow][jumpFindColumn] == 1:
            board[jumpFindRow][move[0] + 1] = 0
    if abs((move[1] - move[3])) == 2 and abs((move[0] - move[2])) == 2 and player == 1 and board[jumpFindRow][jumpFindColumn] == 2:
            board[jumpFindRow][move[0] - 1] = 0
    if debugMove: print("makeMove(", player, move, "board)")
    return board

#.................... 3 ........................................
def validGameMove(player, move, board):
    '''
Determine if the validated move request is a valid game move
   move - a list of integers representing the moves in the order
          [from column, from row, to column, to row]
   player - the player number
   board - the board currently in play
 returns True if the move is valid else False
    '''
    if debugValidate: print(move)
    jumpFindRow = int((move[1]+move[3]) / 2)
    jumpFindColumn = int((move[0]+move[2]) /2)
    if board[move[1]][move[0]] != player:
        return WRONG_PIECE
    elif abs((move[1] - move[3])) > 1 or abs((move[0] - move[2])) > 1:
        if abs((move[1] - move[3])) == 2 and abs((move[0] - move[2])) == 2 and player == 1 and board[jumpFindRow][jumpFindColumn] == 1:
            return JUMP_SELF
        elif abs((move[1] - move[3])) == 2 and abs((move[0] - move[2])) == 2 and player == 1 and board[jumpFindRow][jumpFindColumn] == 0:
            return JUMP_EMPTY
        elif abs((move[1] - move[3])) == 2 and abs((move[0] - move[2])) == 2 and player == 2 and board[jumpFindRow][jumpFindColumn] == 2:
            return JUMP_SELF
        if abs((move[1] - move[3])) == 2 and abs((move[0] - move[2])) == 2 and player == 2 and board[jumpFindRow][jumpFindColumn] == 0:
            return JUMP_EMPTY
        if abs((move[1] - move[3])) == 2 and abs((move[0] - move[2])) == 2 and player == 2 and board[jumpFindRow][jumpFindColumn] == 1:
            return OK_MOVE
        if abs((move[1] - move[3])) == 2 and abs((move[0] - move[2])) == 2 and player == 1 and board[jumpFindRow][jumpFindColumn] == 2:
            return OK_MOVE
        else:
            return ONLY_2
    elif move[1] == move [3] or move[2] == move[0]:
        return ONLY_2
    elif player == 1 and move[3] > move[1]:
        return PLAYER_1_UP
    elif player == 2 and move[3] < move[1]:
        return PLAYER_2_DOWN
    elif board[move[3]][move[2]] != 0:
        return SPACE_TAKEN
    else:
        return OK_MOVE

#==============================================================
# Everything below is test code, DO NOT MODIFY
def getMove(player, board):
    '''
Ask the user for their next move
   player - the player moving next
   board - the current game board
 returns a list of integers representing the moves in the order
          [from row, from column, to row, to column]
    '''
    move = []
    while True:
        try:
            value = input("Player " + str(player) +  " move: ").strip().lower()
            if len(value) == 5:
                startColumn = value[0]
                startRow    = int(value[1])
                endColumn   = value[3]
                endRow      = int(value[4])
                if startColumn >= 'a' and startColumn <= 'h' and \
                   startRow >= 1 and startRow <= 8 and \
                   endColumn >= 'a' and endColumn <= 'h' and \
                   endRow >= 1 and endRow <= 8:
                    move.append(ord(startColumn) - ord('a'))
                    move.append(startRow - 1)
                    move.append(ord(endColumn) - ord('a'))
                    move.append(endRow - 1)
                    status = validGameMove(player, move, board)
                    if status == "OK":
                        return move
                    else:
                        print(status)
                        move.clear()
                        continue
                    
        except ValueError:
            pass
        print("Your entry should be start column/row end column/row (e.g. a0 h7)")

PIECES = [" ", "O", "X"]
def printBoard(board):
    '''
Print the provided board
   board - the board to print
    '''
    for index, rows in enumerate(board):
        print("---------------------------------")
        for space in rows:
            print("| " + PIECES[space] + " ", end = "")
        print("|", index + 1)
    print("---------------------------------")
    print("| a | b | c | d | e | f | g | h |")


def makeList(originalTuple):
    '''
Create a list out of tuple
   originalTuple - the tuple
 returns a list
    '''
    newList = []
    for value in originalTuple:
        newList.append(value)
    return newList

def testInit():
    '''
Test the board initialization
 returns the board if valid, else None
    '''
    board = initializeBoard()
    if len(board) != 8:
        print("initializeBoard() Failed: The board must have 8 rows")
        return
    for index, row in enumerate(board):
        if len(row) != 8:
            print("initializeBoard() Failed: Each row must have 8 columns and row", index, "did not")
            return
        if (index == 0 or index == 2) and row != [0, 2, 0, 2, 0, 2, 0, 2] or \
           index == 1 and row != [2, 0, 2, 0, 2, 0, 2, 0] or \
           (index == 3 or index == 4) and row != [0, 0, 0, 0, 0, 0, 0, 0] or \
           index == 6 and row != [0, 1, 0, 1, 0, 1, 0, 1] or \
           (index == 5 or index == 7) and row != [1, 0, 1, 0, 1, 0, 1, 0]:
            print("initializeBoard() Failed: row", index, " - the setup of the board was invalid, check the assignment description")
            return
    print("Board successfully initialized")
    return board

#The only downside here is you can't move from/to the same spot twice without
# adding to this data structure.  A simple sequence could do for more advanced testing...
TEST_MOVES = {(0, 5, 1, 4): [[0,5,0], [1,4,1]],
              (1, 2, 0, 3): [[1,2,0], [0,3,2]],
              (2, 5, 3, 4): [[2,5,0], [3,4,1]],
              (0, 3, 2, 5): [[0,3,0], [2,5,2], [1,4,0]],
              (3, 6, 1, 4): [[3,6,0], [1,4,1], [2,5,0]],
              (3, 2, 2, 3): [[3,2,0], [2,3,2]],
              (4, 5, 5, 4): [[4,5,0], [5,4,1]]}

def testMoves(board):
    '''
Test if the makeMove() function works properly
 returns True if passed tests
    '''
    success = True
    nextPlayer = 1
    playerShift = 1
    for test in TEST_MOVES:
        if debugMove: printBoard(board)

        move = makeList(test)
        board = makeMove(nextPlayer, move, board)

        for expected in TEST_MOVES[test]:
            actual = board[expected[1]][expected[0]]
            if actual != expected[2]:
                success = False
                print("makeMove() Failed: Your code reported", actual, "at the row", expected[1], "and column", expected[0], "but we expected", expected[2])
                break
        
        if not success: break
        nextPlayer = nextPlayer + playerShift
        playerShift = playerShift * -1
        if debugMove: print()
    if debugMove: printBoard(board)
    if success: print("All move tests passed!")
    return success

VALIDATION_TESTS = {((1,4,0,3), 1) : OK_MOVE, ((0,1,1,2), 2) : OK_MOVE, #Basic move for each player
                    ((1,4,3,2), 1) : OK_MOVE, ((3,4,1,2), 1) : OK_MOVE,  #Jumps for player 1
                    ((2,3,0,5), 2) : OK_MOVE, ((2,3,4,5), 2) : OK_MOVE, #Jumps for player 2
                    ((0,0,1,1), 1) : WRONG_PIECE, ((0,0,1,1), 2) : WRONG_PIECE, # Empty square each player
                    ((0,1,1,2), 1) : WRONG_PIECE, ((1,6,0,5), 2) : WRONG_PIECE, # Moving the other player's piece
                    ((1,6,4,5), 1) : ONLY_2, ((6,1,1,1), 2) : ONLY_2, # Horizontally
                    ((0,7,0,3), 1) : ONLY_2, ((7,0,4,3), 2) : ONLY_2, # Vertically
                    ((1,4,0,5), 1) : PLAYER_1_UP, ((2,3,1,2), 2) : PLAYER_2_DOWN,
                    ((1,4,2,3), 1) : SPACE_TAKEN, ((2,3,1,4), 2) : SPACE_TAKEN,
                    ((0,7,2,5), 1) : JUMP_SELF, ((3,0,1,2), 2) : JUMP_SELF,
                    ((4,7,2,5), 1) : JUMP_EMPTY, ((2,1,0,3), 2) : JUMP_EMPTY}

def testValidation(board):
    '''
Test if the validGameMove() function works properly
 returns True if passed tests
    '''
    if debugValidate: printBoard(board)
    success = True
    for test in VALIDATION_TESTS:
        move = test[0]
        answer = validGameMove(test[1], move, board)
        if (answer != VALIDATION_TESTS[test]):
            success = False
            print ("Call to validGameMove(", move, ",", test[1],
                   ", board) failed as your code returned \"",
                   answer, "\" but we expected \"",
                   VALIDATION_TESTS[test], "\"")

    if success: print("All validations passed!")
    return success

def playGame():
    '''
Prompts the user to play checkers against themselves
    '''
    board       = initializeBoard()
    nextPlayer  = 1
    playerShift = 1
    for count in range(moveLimit):
        printBoard(board)
        move = getMove(nextPlayer, board)
        board = makeMove(nextPlayer, move, board)
        nextPlayer = nextPlayer + playerShift
        playerShift = playerShift * -1
        print()

# Only run this code below if this is called as the main, not imported
if __name__ == '__main__':
    board = testInit();
    if board != None:
        testMoves(board)
        if runValidationTests:
            testValidation(board)
        if playAfterTest:
            playGame()
