# Yvonne Aime, COP2500, July 10 2023
# High Low Game

import random





# anything that is not in the range of 1 - 100 (could be 101,-4...)  
# (setting it to equal to false for the while loop) 
# number is outside the loop'
play_game = True
while(play_game == True):
    # chooses a number 1 - 100 listed as (1,100)
    hidden_num = random.randint(1,100)
    guess = -1

while(hidden_num != guess):
    guess = int(input("What is your guess\n"))

    if(guess == hidden_num):
        print("You got it!!")
    elif(guess > hidden_num):
        print("Guess lower")
    else:
        print("Guess higher")
again = input("Would you like to play again?\n")
if(again == "Yes" or again == "yes"):