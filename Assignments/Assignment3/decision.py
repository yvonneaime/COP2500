# Yvonne Aime
# COP2500
# July 5 2023

# Assignment 3 - Food Decisions


# Budget - as a float (input())
budget = float(input("How much money do we have to spend?\n\n"))
# States Restaurant Options
options = int(input("Where would you like to go?\n" 
                    "1. Hot Dog Heaven\n" "2. Hawkers\n" "3. Black Bean Deli\n"))
total = budget + 1

while(budget < total):
    print(options)

    # Option 1 - Hot Dog Heaven
    if (options == 1):
        print("You chose option 1 (Hot Dog Heaven) \nThey sell the following food items:")       
        print("\t1. Chicago Hot Dog - $4.50\n \t2. Fries - $2.75\n")
        what_choice = int(input("What would you you like to buy?\n"))
        food_count = int(input("How many would you like to buy?\n"))
        if (what_choice == 1):
            total = 4.50 * food_count
        if (what_choice == 2):
            total = 2.75 * food_count
        print("\nThat would cost $%.2f"%total)

    # Option 2 - Hawkers
    if (options == 2):
        print("You chose option 2 (Hawkers) \nThey sell the following food items:")       
        print("\t1. Chicken Dumplings - $10.00\n \t2. Roti Canai - $9.00\n")
        what_choice = int(input("What would you you like to buy?\n"))
        food_count = int(input("How many would you like to buy?\n"))
        if (what_choice == 1):
            total = 10.00 * food_count
        if (what_choice == 2):
            total = 9.00 * food_count
        print("\nThat would cost $%.2f"%total)
    
    # Option 3 - Black Bean Deli
    if (options == 3):
        print("You chose option 3 (Black Bean Deli) \nThey sell the following food items:")       
        print("\t1. Dark Chicken Platter - $14.60\n \t2. Yuca Fries - $7.85\n")
        what_choice = int(input("What would you you like to buy?\n"))
        food_count = int(input("How many would you like to buy?\n"))
        if (what_choice == 1):
            total = 14.60 * food_count
        if (what_choice == 2):
            total = 7.85 * food_count
        print("\nThat would cost $%.2f"%total)

    # Print final statements: (Either you got it or you don't)
    if(budget > total):
        print("You have enough!\n✩ Enjoy! ✩ ")
    else:
        print("You dont have enough.")
        

