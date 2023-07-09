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

# Write your mad libs program here

story= ("My first coding class was exciting.That's where I met Sylvia, the girl with the red hat. We both liked swimming over the weekends.It was quite intresting to find out our favourite movie series was 'Game of Thrones'.We planned to go watch the new episode on Tuesday at the cinema.It was funny that she bought 3 buckets of popcorn!")

#Prompt the user to give input

favourite_subject =input("Enter your favourite subject: ")
name = input("Enter your favourite celebrity: ")
colour = input("Enter a colour: ")
hobby = input("Enter your pass time activity: ")
movie = input("Enter a series you just watched: ")
day = input("Enter a day of the week: ")
number = input("Enter you current age: ")

#Store all the responses the user entered

madlib_story = f"My first {favourite_subject} class was exciting.That's where I met {name}, the girl with the {colour} hat. We both liked {hobby} over the weekends.It was quite intresting to find out our favourite movie series was '{movie}'.We planned to go watch the new episode on {day} at the cinema.It was funny that she bought {number} buckets of popcorn!"

#output the madlib_story
