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

