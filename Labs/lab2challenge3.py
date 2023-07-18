# Yvonne Aime, COP2500, July 4 2023
# Lab 2 - Challenge 3

# Write a function that takes in the number of the party and asks them how many
# sporting events they attended at UCF.  Total up the amount, and retun the amount.
def sports_dinner(people):
    total = 0

    for i in range(people):
        attend = (int(input("How many sporting events they attended at UCF?\n")))
        total += attend
    return total


# Write a function that waiting for someone to say a lucky number.  This lucky
# number will be passed in as a parameter.  They must keep guessing until 
# they get it correct.  When they get it correct turn "Got it!"

def table_game(lucky_number):
    # Asks user for number
    num = int(input("What's your number?\n"))

    while(num != lucky_number):
        num = int(input("What's your number?\n"))
    return "You got it!!"

print("sports_dinner(people):", sports_dinner(3))
print("sports_dinner(people):", sports_dinner(2))

print("table_game(lucky_number):", table_game(3))
print("table_game(lucky_number):", table_game(8))