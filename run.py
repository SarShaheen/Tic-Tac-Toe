# Tic-Tac-Toe

import random

print("Welcome To Tic-Tac-Toe!")


def select_player_letter():
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


def create_board(board):
    # This prints out the board.
    # "board" is a list of 10 strings (ignoring index 0).

    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def first_move():
    # Chooses which player goes first
    if random.randint(0, 1) == 0:
        return "Computer"
    else:
        return "Player"


def make_move(board, letter, move):
    board[move] = letter


def winner(board, letter):
    # Function returns true if given board and players letter,
    # that player has won.
    if board[7] == letter and board[8] == letter and board[9] == letter:
        return True
    elif board[4] == letter and board[5] == letter and board[6] == letter:
        return True
    elif board[1] == letter and board[2] == letter and board[3] == letter:
        return True
    elif board[7] == letter and board[4] == letter and board[1] == letter:
        return True
    elif board[8] == letter and board[5] == letter and board[2] == letter:
        return True
    elif board[9] == letter and board[6] == letter and board[3] == letter:
        return True
    elif board[7] == letter and board[5] == letter and board[3] == letter:
        return True
    elif board[9] == letter and board[5] == letter and board[1] == letter:
        return True
    else:
        return False


def copy_board(board):
    # Copys board list and returns it
    board_copy = []
    for i in board:
        board_copy.append(i)
    return board_copy


def free_space(board, move):
    # If space is free on the board, returns true
    return board[move] == " "


def player_move(board):
    # Let's player make their move
    move = " "
    while move not in "1 2 3 4 5 6 7 8 9".split() or not free_space(board, int(move)):
        print("Where is your next move? (1-9)")
        move = input()
    return int(move)


def make_random_move(board, move_list):
    # Returns a valid move from the list on the board
    # Returns none if no valid move
    potential_moves = []
    for i in move_list:
        if free_space(board, i):
            potential_moves.append(i)

    if len(potential_moves) != 0:
        return random.choice(potential_moves)
    else:
        return None


def computer_move(board, computer_letter):
    # Determines where to return a move given the board and computers letter
    if computer_letter == "X":
        player_letter = "O"
    else:
        player_letter = "X"

    # Algorithm for Tic-Tac-Toe AI:
    # Checks if computer can win in next move
    for i in range(1, 10):
        board_copy = copy_board(board)
        if free_space(board_copy, i):
            make_move(board_copy, computer_letter, i)
            if winner(board_copy, computer_letter):
                return i

    # Checks if player can win in next move and block the computer
    for i in range(1, 10):
        board_copy = copy_board(board)
        if free_space(board_copy, i):
            make_move(board_copy, player_letter, i)
            if winner(board_copy, player_letter):
                return i

    # Checks if one of the corners is free to move to
    move = make_random_move(board, [1, 3, 7, 9])
    if move is not None:
        return move

    # Checks if center is free to move to
    if free_space(board, 5):
        return 5

    # Moves on one of the sides
    return make_random_move(board, [2, 4, 6, 8])


def board_full(board):
    # If all spaces are taken, returns true otherwise returns false
    for i in range(1, 10):
        if free_space(board, i):
            return False
    return True


while True:
    # Resets the board
    the_board = [" "] * 10
    player_letter, computer_letter = select_player_letter()
    turn = first_move()
    print("The " + turn + " will go first.")
    playing_game = True

    while playing_game:
        if turn == "player":
            # players turn
            create_board(the_board)
            move = player_move(the_board)
            make_move(the_board, player_letter, move)

            if winner(the_board, player_letter):
                create_board(the_board)
                print("Yay! You have won!")
                playing_game = False
            else:
                if board_full(the_board):
                    create_board(the_board)
                    print("The game is a tie!")
                    break
                else:
                    turn = "computer"

        else:
            # Computers turn
            move = computer_move(the_board, computer_letter)
            make_move(the_board, computer_letter, move)

            if winner(the_board, computer_letter):
                create_board(the_board)
                print("The computer has won, you lose!")
                playing_game = False
            else:
                turn = "player"

    print("Do you want to play again? (yes or no)")
    if not input().lower().startswith("y"):
        break
