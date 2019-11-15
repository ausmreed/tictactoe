# This is the main gameplay of the Tic-Tac-Toe game I devloped.

blank_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

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

def check_if_square_filled(number,board):
    valid = 0
    if number == 7 and board[0][0] == " ":
        valid = 1
    elif number == 8 and board[0][1] == " ":
        valid = 1
    elif number == 9 and board[0][2] == " ":
        valid = 1
    elif number == 4 and board[1][0] == " ":
        valid = 1
    elif number == 5 and board[1][1] == " ":
        valid = 1
    elif number == 6 and board[1][2] == " ":
        valid = 1
    elif number == 1 and board[2][0] == " ":
        valid = 1
    elif number == 2 and board[2][1] == " ":
        valid = 1
    elif number == 3 and board[2][2] == " ":
        valid = 1
    return valid

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
    elif number == 3:
        board[2][2] = player
    else:
        print ("Not a valid number, please enter a number 1-9, Try again")

    return board

def check_if_three_in_row(player, board, move):
    #Go through all possible combinations?
    valid = 0
    if move == 1:
        if (board[0][0] == player and board[1][0] == player) or (board[1][1] == player and board[0][2] == player) or (board[2][1] == player and board[2][2] == player):
            valid = 1
    elif move == 2:
        if (board[2][0] == player and board[2][2] == player) or (board[1][1] == player and board[0][1] == player):
            valid = 1
    elif move == 3:
        if (board[2][0] == player and board[2][1] == player) or (board[1][2] == player and board[0][2] == player) or (board[1][1] == player and board[0][0] == player):
            valid = 1
    elif move == 4:
        if (board[1][1] == player and board[1][2] == player) or (board[0][0] == player and board[2][0] == player):
            valid = 1
    elif move == 5:
        if (board[0][0] == player and board[2][2] == player) or (board[0][1] == player and board[2][1] == player) or (board[0][2] == player and board[2][0] == player) or (board[1][0] == player and board[1][2] == player):
            valid = 1
    elif move == 6:
        if (board[1][0] == player and board[1][1] == player) or (board[0][2] == player and board[2][2] == player):
            valid = 1
    elif move == 7:
        if (board[0][1] == player and board[0][2] == player) or (board[1][1] == player and board[2][2] == player) or (board[1][0] == player and board[2][0] == player):
            valid = 1
    elif move == 8:
        if (board[0][0] == player and board[0][2] == player) or (board[1][1] == player and board[2][1] == player):
            valid = 1
    elif move == 9:
        if (board[0][0] == player and board[0][1] == player) or (board[1][1] == player and board[2][0] == player) or (board[1][2] == player and board[2][2] == player):
            valid = 1
    return valid



# Welcomeing Message!
print("Hello! Welcome to Austin's Tic-Tac-Toe Game")

# Create a way to alternate moves. Max number of moves in a tic-tac-toe game is 9.
# Specify which mover will go first.
moveorder = []
if input('Which player will go first, X or O').upper() == 'X':
    for i in range(5):
        moveorder.append('X')
        moveorder.append('O')
else:
    for i in range(5):
        moveorder.append('O')
        moveorder.append('X')

# Create move (turn) index, allow user to enter number, put X or O in board (with function above)
# and print out board again.
turn = 1
turn_index = turn - 1

while turn_index <= 8:
    print("Move {}".format(turn))
    print("{}, it's your turn!".format(moveorder[turn_index]))
    print('{}, please enter the position 1-9, corresponding to your num pad, that you would like to play'.format(moveorder[turn_index]))
    position = int(input())
    if check_if_square_filled(position, board) == 1 and check_if_three_in_row(moveorder[turn_index], board, position) != 1 :
        edit_board(board, position, moveorder[turn_index])
        print_board(board)
        turn_index +=1
        turn += 1
    elif check_if_square_filled(position, board) == 1 and check_if_three_in_row(moveorder[turn_index], board, position) == 1 :
        edit_board(board, position, moveorder[turn_index])
        print_board(board)
        print("Congrats {}, you got three in a row and won!".format(moveorder[turn_index]))
        break

    else:
        print("Space already filled! Try again")


if turn == 10: #And check if 3 in a row exists!
    print("A Tie!")
    print("Would you like to play again?")
else:
    print("Would you like to play again?")
