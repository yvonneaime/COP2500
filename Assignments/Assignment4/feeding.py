# Yvonne Aime
# COP2500
# July 12 2023

# Assignment 4 - Feeding Roommates

import random 

#Header for program
print("Welcome!")

# Calculate # of calories 
def grams_to_cal(grams):
    pass
    # 30% (protein) of grams * 4cal = 1.2 cal
    # 20% (vegetables) of grams * 1cal = 0.2 cal
    # 50% (carbohydrates) of grams * 4cal = 2 cal
    # Average balanced meal there 3.4 calories in a gram

def roommate_1(meals):
    # Random meal number generated to decide how many meals for that day (2-7 meals)
    meal_num =  random.randint(2, 7)

    # Header for Roomate #1
    print("Roomate #1\nLooks like you are eating",meal_num,"meals today.")
    meals = 0
    for i in range(meal_num):
       grams_per_meal = int(input("How many grams was meal #"+ str(i+1)+ "\n"))
       meals += grams_per_meal 
    return meals
    

#Ask random number
# loop that many times
    # Ask the user for an integer
    # total the amount of cal
# return cal

def roommate_2():
    print("Roomate #2\n")
    large_grams = int(input("How may grams was your large meal?\n"))
    

    # ask user for how much they ate that day 
    # convert it to cals using function
    # return that amount
def roommate_3():
    pass
    # Print out 3 options
    # if options and ask which one
    # ask how much they used
    # if option 1 or 3
        #add the amount times 4
    # otherwise
        # add the amount to the total
    # do above 3 times
    # return total 

# No code outside of the function
def main():
    room1_cal = roommate_1()

    if(room1_cal >= 2500):
        print("Roomate 1 ate",room1_cal )
    else: 
        print("Didnt eat enuff",room1_cal )


print("roommate_1(meals):", roommate_1(3))