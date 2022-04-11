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
    ret boardCopy