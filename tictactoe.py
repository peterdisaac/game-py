# Peter Isaac

# Tic Tac Toe Game
# Two Player Game

import sys
import os
import platform
from os import system
import math

COMPUTER = +1
PLAYER = 0

# Two Player Functions
# ----------------------

def start_two_player_game(board):
    '''
    Control method:
    Alternates back and forth between players
    X ALWAYS goes first
    '''
    move = 0
    won = False
    turn = -1 # Positive 1 is a move for X, negative 1 is a move for O
    print("Welcome to Tic-Tac-Toe: Two Player Mode")
    instructions()

    while not won:
        clear_screen()
        turn = turn * (-1)
        print_board(board)
        move += 1
        if move > 9 and not check_win(board):
            draw(board)
        elif get_turn(turn, board):
            if move > 3:
                won = check_win(board)
    if won:
        end_game(turn, board)


def draw():
    '''
    Handles the case when the game is over, but no one won
    '''
    print("\n")
    print("=================")
    print("Draw.  No winner")
    exit()


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


def end_game(turn, board):
    '''
    Handles the case when the game ends because someone won
    :param turn: which player has won, X or O
    :param board: the current state of the game
    :return nothing
    '''
    print("\n")
    print("====================")
    print("     Game Over.")
    if turn == 1:
        print("     X won!")
    else:
        print("     O won!")
    print("")
    print_board(board)


def instructions():
    '''
    Prints the instructions for playing the game
    '''
    print("INSTRUCTIONS")
    print("Enter the corresponding number of the cell you want to make your move in")
    print("        1 | 2 | 3 ")
    print("       ------------")
    print("        4 | 5 | 6 ")
    print("       ------------")
    print("        7 | 8 | 9 ")
    print("\n\n")


def print_board(gameboard):
    '''
    Prints the current state of the game
    :param gameboard: the current state of the game
    '''
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
    '''
    Clears the screen to make for a more visually appealing game
    '''
    operating_system = platform.system().lower()
    if "windows" in operating_system:
        system('cls')
    else:
        system('clear')


def main():
    board = [[-1 for x in range(3)] for y in range(3)]
    start_two_player_game(board)


if __name__ == "__main__":
    main()
