from helper import Helper
import random

dimension = 1
while 3 > dimension or dimension > 5:
    try:
        dimension = int(input("Enter the Dimension of the Board b/w 3 and 5:"))
    except ValueError:
        print("Input can only be integer")
first_turn_choice = random.randint(0, 1)
curr_symbol = "X" if first_turn_choice == 0 else "O"  # Randomly Giving First Turn to either X or O
player_dict = {"Player1": curr_symbol, "Player2": "X" if curr_symbol == "O" else "O"}  # Initializing Player Dict
print(f"Player 1 Turn {curr_symbol}:")
matrix = Helper.initialize_board(dimension)  # Initializing Player Board
while True:
    curr_player = "Player1" if curr_symbol == player_dict["Player1"] else "Player2"
    Helper.print_board(matrix, dimension)
    isUpdated = False
    while not isUpdated:  # Getting User Input and Updating Game Board
        letter_input = input(f"Enter the letter at which You want to place {curr_symbol}:").lower()
        isUpdated = Helper.update_matrix(matrix, dimension, letter_input, curr_symbol) if len(
            letter_input) == 1 else print("Only One letter must be input")
    isWin = Helper.check_win(dimension, curr_symbol, matrix)  # Checking if the User Win
    if isWin:
        Helper.print_board(matrix, dimension)
        print(f"Congratulations!! {curr_player} Won")
        break
    curr_symbol = "X" if curr_symbol == "O" else "O"  # Updating Player's Turn
