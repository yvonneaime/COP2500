# Yvonne Aime
# COP2500
# July 12 2023

# Assignment 4 - Feeding Roommates

import random 

#Header for program
print("Welcome!")

# Calculate # of calories 
def grams_to_cal(grams):
    # 30% (protein) of grams * 4cal = 1.2 cal
    # 20% (vegetables) of grams * 1cal = 0.2 cal
    # 50% (carbohydrates) of grams * 4cal = 2 cal
    # Average balanced meal there 3.4 calories in a gram
    return grams * 3.4 

def roommate_1():
    # Random meal number generated to decide how many meals for that day (2-7 meals)
    meal_num =  random.randint(2, 7)
    
    # Header for Roomate #1
    print("Roomate #1\nLooks like you are eating",meal_num,"meals today.")
    meals = 0
    
    for i in range(meal_num):
       grams_per_meal = float(input("How many grams was meal #"+ str(i+1)+ "?\n"))
       meals += grams_per_meal 
    # Calulates average Calories 
    meals = meals * 3.4
    return meals
    

def roommate_2():
    # Header for Roomate #2
    print("Roomate #2")
    # Integer Input - grams in large  meal
    large_grams = float(input("How many grams was your large meal?\n"))
    # Grams converted to calories 
    large_grams = large_grams * 3.4
    return large_grams

def roommate_3():
    # Header for Roomate #3
    print("Roomate #3\n")

    # Lists main food group options
    total = 0
    for i in range(3):
        meal_options = int(input("What are you eating for meal #"+ str(i+1)+ 
                                 "?\n1 - Protein \n2 - Veggie \n3 - Carb\n"))
        food_intake = float(input("\nHow much did you eat?"))
        if(meal_options == 1 or meal_options == 3 ):
            calorie = 4 
        elif(meal_options == 2):
            calorie = 1
        total = calorie * food_intake
    return total
        
        

# No code outside of the function
def main():
    room1_cal = roommate_1()

    if(room1_cal >= 2500):
        print("Roomate 1 ate",room1_cal )
    else: 
        print("Didnt eat enuff",room1_cal )


print("roommate_1():", roommate_1(), "\n")
print("roommate_2():", roommate_2(), "\n")
print("roommate_3():", roommate_3(), "\n")