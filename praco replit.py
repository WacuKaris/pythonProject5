# # this is a multiline string; it starts with three quotes
blank_board = """
  1   2   3
--- --- ---
 1   |   |  |
 --- --- ---
 2   |   |  |
 --- --- ---
 3   |   |  |
 """
# Accept the user's input for the game.
name = input("What is your name? ")
print(f"Welcome to Tic Tac Toe, {name}. Here is our playing board: ")

# #Print the board
print(blank_board)
# Accept the user's input of the playing position
position = (input("Enter a position (i.e.,1,1): "))
print(position)