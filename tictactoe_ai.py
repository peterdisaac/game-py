import sys
import os
import platform
from os import system
from random import choice

COMPUTER = 1
PLAYER = 0
PLAYER_CHOICE = -1 # Set to 1 for X and 0 for O

def start_one_player_game(board):
    player = ''
    move = 0
    won = False
    first = 0

    print("Welcome to Tic-Tac-Toe: One Player Mode")
#   instructions()

    player = ''
    while player != 'O' and player != 'X':
        try:
            player = raw_input("Choose X or O\nChosen: ").upper()
        except KeyboardInterrupt:
            print('\nExiting...')
            exit()
        except:
            print(player)
            print("Invalid choice. Try again.")

    if player == 'X':
        computer = 0
        player = 1
        first = 1
        PLAYER_CHOICE = 1
    else:
        computer = 1
        player = 0
        PLAYER_CHOICE = 0

    while not check_win(board):
        print_board(board)
        if first == 1:
            player_turn(player, board)
            print_board(board)
            first = 0

        computer_turn(board)
        player_turn(player, board)


def check_win(board):
    '''
    Check the current state of the board to see if anyone as won
    :param board: current state of the game
    :return true if someone won the game, false if not
    '''
    # Check horizontal and vertical
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != -1:
            return True
        elif board[0][i] == board[1][i] == board[2][i] != -1:
            return True

    # Check diagonal
    if board[0][0] == board[1][1] == board[2][2] != -1:
        return True
    elif board[0][2] == board[1][1] == board[2][0] != -1:
        return True
    return False


def player_turn(turn, board):
    get_turn(turn, board)


def get_turn(turn, board):
    '''
    Recieves a integer input from the user and converts into 2d array offsets
    
    :param turn: which player(X or O) is making a move
    :param board: current board state
    :return: true if a move was made
    '''
    if turn == 1:
        msg = "Select a cell for X: "
    else:
        msg = "Select a cell for O: "

    move = get_input(msg)
    x, y = get_coordinates(move)

    if board[x][y] != -1:
        print("Invalid cell.  Already marked.  Please try again")
        get_turn(turn, board)
    else:
        if turn == 1:
            board[x][y] = 1
            return True
        else:
            board[x][y] = 0
            return True


def get_coordinates(move):
    '''
    :param move: An integer representing which cell the player wants to make his or her move to
    :return: the coordinates into the 2d game board as a tuple
    '''
    if move % 2 == 0:
        # Number is even
        if move % 3 == 2:
            y = 1
            if move == 2:
                x = 0
            else:
                x = 2
        elif move % 3 == 1:
            x = 1
            y = 0
        elif move % 3 == 0:
            x = 1
            y = 2
    else:
        # Number is odd
        if move % 4 == 1:
            if move == 1:
                x = 0
                y = 0
            elif move == 5:
                x = 1
                y = 1
            else:
                x = 2
                y = 2
        else:
            if move == 3:
                x = 0
                y = 2
            else:
                x = 2
                y = 0
    return x, y


def get_input(msg):
    '''
    :param msg: Message displayed to the user, identifies between X and O
    :return the integer bewteen 1 and 9 that the user selected
    '''
    userInput = ''
    while userInput is not int:
        try:
            userInput = int(raw_input(msg))
            break
        except KeyboardInterrupt:
            print('\nExiting...')
            exit()
        except ValueError:
            print("You did not enter a number, please try again")

    if userInput < 1 or userInput > 9:
        print("Your entry is outside the bounds.  Please enter a number between 1 and 9")
        get_input(msg)
    else:
        return userInput


def computer_turn(board):
    depth = len(blank_position(board))
    if depth == 0 or check_winner(board, COMPUTER):
        return

    print("Computer turn. Thinking...")
    #clear_screen()
    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, COMPUTER, depth)
        x, y = move[0], move[1]
    board[x][y] = COMPUTER
    print_board(board)


def minimax(board, player, depth):
    """
    player - the computer
    """
    if player == COMPUTER:
        best_move = [-1, -1, -100000]
    else:
        best_move = [-1, -1, +100000]

    if depth == 0 or check_win(board):
        score = heuristic(board, player)
        return [-1, -1, score]

    for move in blank_position(board):
        x, y, = move[0], move[1]
        board[x][y] = player
        score = minimax(board, -player, depth-1)
        board[x][y] = -1
        score[0], score[1] = x, y

    if player == COMPUTER:
        if score[2] > best_move[2]:
            best_move = score
    else:
        if score[2] < best_move[2]:
            best_move = score
    return best_move


def blank_position(board):
    cells = []
    for x, row in enumerate(board):
        for y, cell in enumerate(row):
            if cell == -1: cells.append([x, y])
    return cells


def heuristic(board, player):
    if check_winner(board, COMPUTER):
        score = +1
    elif check_winner(board, PLAYER):
        score = -1
    else:
        score = 0
    return score


def check_winner(board, player):
    '''
    Checks if the player won, returns True if they did
    '''
    winning_board = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    if [player, player, player] in winning_board:
        return True
    else:
        return False


def print_board(gameboard):
    for i in range(3):
        sys.stdout.write(" ")
        for j in range(3):
            if gameboard[i][j] == 1:
                sys.stdout.write('X')
            elif gameboard[i][j] == 0:
                sys.stdout.write('O')
            else:
                sys.stdout.write(' ')
            if j != 2:
                sys.stdout.write(" | ")
        print("")
        if i != 2:
            print("-----------")


def clear_screen():
    operating_system = platform.system().lower()
    if "windows" in operating_system:
        system('cls')
    else:
        system('clear')

        
def main():
    board = [[-1 for x in range(3)] for y in range(3)]

    start_one_player_game(board)


if __name__ == "__main__":
    main()

                                                                                                                                                             293,0-1       Bot
