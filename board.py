# This is the main gameplay of the Tic-Tac-Toe game I devloped.


board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


# Outlining what the board will look like.
# SPACE | SPACE | SPACE
# ---------------------
# SPACE | SPACE | SPACE
# ---------------------
# SPACE | SPACE | SPACE

# Corresponds to:
# 7 | 8 | 9
# 4 | 5 | 6
# 1 | 2 | 3

# Define a function that will print out a tic tac toe board when given a "raw matrix"

def print_board(board):
    print(' {} | {} | {} '.format(board[0][0], board[0][1], board[0][2]))
    print('-----------')
    print(' {} | {} | {} '.format(board[1][0], board[1][1], board[1][2]))
    print('-----------')
    print(' {} | {} | {} '.format(board[2][0], board[2][1], board[2][2]))
print_board(blank_board)

# Define a function to modify board (make a move):
def edit_board(board, number, player):
    if number == 7:
        board[0][0] = player
    elif number == 8:
        board[0][1] = player
    elif number == 9:
        board[0][2] = player
    elif number == 4:
        board[1][0] = player
    elif number == 5:
        board[1][1] = player
    elif number == 6:
        board[1][2] = player
    elif number == 1:
        board[2][0] = player
    elif number == 2:
        board[2][1] = player
    elif number == 1:
        board[2][2] = player
    else print("Not a valid number, please enter a number 1-9")
        edit_board(board, number, player)
    return board


# Welcomeing Message!
print("Hello! Welcome to Austin's Tic-Tac-Toe Game")

# Create a way to alternate moves. Max number of moves in a tic-tac-toe game is 9.
# Specify which mover will go first.
moveorder = []
if input('Which player will go first, X or O') == 'X':
    for i in range(5):
        moveorder.append('X')
        moveorder.append('O')
else:
    for i in range(5):
        moveorder.append('O')
        moveorder.append('X')
print('Player {}, please enter the position 1-9, corresponding to your num pad, that you would like to play')
