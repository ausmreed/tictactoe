from board import play_game

print("Hello! Welcome to Austin's Tic-Tac-Toe Game")
tie_game = play_game()

if tie_game == 0:
    play_again = input("Game over! Would you like to play again? Y/N")
    if play_again.upper() == "Y":
        play_game()

elif tie_game == 1:
    play_again = input("Tie game! Would you like to play again? Y/N")
    if play_again.upper() == 'Y':
        play_game()
