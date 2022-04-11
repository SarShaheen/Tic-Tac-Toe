# Tic-Tac-Toe


import random


def selectPlayerLetter():
    # Let's the player pick what letter they want to be.
    # Returns a list with the players letter as the first item and
    # the computers letter as the second item.

    letter = " "
    while not (letter == 'X' or letter == 'O'):
        print("Do you want to be X or O?")
        letter = input().upper()

    if letter == 'X':
        return ["X", "O"]
    else:
        return ["O", "X"]


def theBoard(board):
    # This prints out the board.
    # "board" is a list of 10 strings (ignoring index 0).

    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def firstMove():
    # Chooses which player goes first
    if random.randint(0, 1) == 0:
        return "Computer"
    else:
        return "Player"


def makeMove(board, letter, move):
    board[move] = letter


def Winner(board, letter):
    # Function returns true if given board and players letter,
    # that player has won.
    return ((board[7] == letter and board[8] == letter and board[9] == letter
     or
    (board[4] == letter and board[5] == letter and board[6] == letter) or
    (board[1] == letter and board[2] == letter and board[3] == letter) or
    (board[7] == letter and board[4] == letter and board[1] == letter) or
    (board[8] == letter and board[5] == letter and board[2] == letter) or
    (board[9] == letter and board[6] == letter and board[3] == letter) or
    (board[7] == letter and board[5] == letter and board[3] == letter) or
    (board[9] == letter and board[5] == letter and board[1] == letter))


def copyBoard(board):
    # Copys board list and returns it
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def freeSpace(board, move):
    # If space is free on the board, returns true
    return board[move] == " "

def playerMove(board):
    # Let's player make their move
    move = " "
    while move not in "1 2 3 4 5 6 7 8 9".split() or not freeSpace(board, int(move)):
        print("Where is your next move? (1-9)")
        move = input()
    return int(move)

def makeRandomMove(board, moveList):
    # Returns a valid move from the list on the board
    # Returns none if no valid move
    potentialMoves = []
    for i in moveList:
        if freeSpace(board, i):
            potentialMoves,append(i)

    if len(potentialMoves) != 0:
        return random.choice(potentialMoves)
    else:
        return None

def computerMove(board, computerLetter):
    # Determines where to return a move given the board and computers letter
    if computerLetter == "X":
        playerLetter = "O"
    else:
        playerLetter = "X"

    # Algorithm for Tic-Tac-Toe AI:
    # Checks if computer can win in next move
    for i in range(1, 10):
        boardCopy = copyBoard(board)
        if freeSpace(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if Winner(boardCopy, computerLetter):
                return i

    # Checks if player can win in next move and block the computer
    for i in range(1, 10):
        boardCopy = copyBoard(board)
        if freeSpace(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if Winner(boardCopy, playerLetter):
                return i

    # Checks if one of the corners is free to move to
    move = makeRandomMove(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Checks if center is free to move to
    if freeSpace(board, 5):
        return 5

    # Moves on one of the sides
    return makeRandomMove(board, [2, 4, 6, 8])
    

