import random


def draw_board(board):
    """
    'board' is a list of strings representing the board display.
    """
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def input_player_letter():
    """
    Lets player type which letter they want to be. Returns the
    player's letter as first item and the computer's as the second.
    """
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?\n')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def who_goes_first():
    """
    Randomly choose which player makes first move.
    """
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def make_move(board, letter, move):
    """ Making a move on board. """
    board[move] = letter


def is_winner(brd, letter):
    """
    Given a board and a player's letter, function returns True if
    that player has won.
    """
    return ((brd[7] == letter and brd[8] == letter and brd[9] == letter) or
            (brd[4] == letter and brd[5] == letter and brd[6] == letter) or
            (brd[1] == letter and brd[2] == letter and brd[3] == letter) or
            (brd[7] == letter and brd[4] == letter and brd[1] == letter) or
            (brd[8] == letter and brd[5] == letter and brd[2] == letter) or
            (brd[9] == letter and brd[6] == letter and brd[3] == letter) or
            (brd[7] == letter and brd[5] == letter and brd[3] == letter) or
            (brd[9] == letter and brd[5] == letter and brd[1] == letter))


def get_board_copy(board):
    """ Copy the board list and return it."""
    board_copy = []
    for i in board:
        board_copy.append(i)
    return board_copy


def space_free(board, move):
    """Return True if the move is free on the board."""
    return board[move] == ' '


def player_move(board):
    """ Let the player enter their move."""
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() \
            or not space_free(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)


def random_move(board, moves_list):
    """ Returns a valid move from list on the passed board.
    Returns None if there is no valid move."""
    potential_moves = []
    for i in moves_list:
        if space_free(board, i):
            potential_moves.append(i)
    if len(potential_moves) != 0:
        return random.choice(potential_moves)


def computer_move(board, computer_letter):
    """ Given a board and computer's letter, determine where to move to."""
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'
    # Here is the algorithm for our Tic-Tac-Toe AI:
    # This check if we can win with our next move.
    for i in range(1, 10):
        board_copy = get_board_copy(board)
        if space_free(board_copy, i):
            make_move(board_copy, computer_letter, i)
            if is_winner(board_copy, computer_letter):
                return i
    # This checks if player could win on their next move.
    for i in range(1, 10):
        board_copy = get_board_copy(board)
        if space_free(board_copy, i):
            make_move(board_copy, player_letter, i)
            if is_winner(board_copy, player_letter):
                return i
    # Tries to take one of the corners, if free.
    move = random_move(board, [1, 3, 7, 9])
    if move is not None:
        return move
    # Tries to take the center, if it's free.
    if space_free(board, 5):
        return 5
    # Move on one of the sides.
    return random_move(board, [2, 4, 6, 8])


def board_full(board):
    """ Returns True if all spaces on the board have been taken."""
    for i in range(1, 10):
        if space_free(board, i):
            return False
    return True


print('\nWelcome to Tic-Tac-Toe!\n')
print('Rules: The spaces on the board are laid out as a keyboard number pad.')
print('Using the numbers 1 - 9, you may place your mark on the board until')
print('one of you gets 3 in a row.\n')
while True:
    # Reset the board.
    theBoard = [' '] * 10
    player_letter_one, computer_letter_one = input_player_letter()
    TURN = who_goes_first()
    print('The ' + TURN + ' will go first.')
    PLAYING_GAME = True
    while PLAYING_GAME:
        if TURN == 'player':
            # Player's turn
            draw_board(theBoard)
            MOVE = player_move(theBoard)
            make_move(theBoard, player_letter_one, MOVE)
            if is_winner(theBoard, player_letter_one):
                draw_board(theBoard)
                print('Yay! You have won the game!')
                PLAYING_GAME = False
            else:
                if board_full(theBoard):
                    draw_board(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    TURN = 'computer'
        else:
            # Computer's turn
            move_comp = computer_move(theBoard, computer_letter_one)
            make_move(theBoard, computer_letter_one, move_comp)
            if is_winner(theBoard, computer_letter_one):
                draw_board(theBoard)
                print('The computer has won! You lose.')
                PLAYING_GAME = False
            else:
                if board_full(theBoard):
                    draw_board(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    TURN = 'player'
    print('Want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break
