# Assignment 3 - Food Decisions
# Yvonne Aime, COP2500, July 5 2023

# First Statement 
budget = float(input("How much money do we have to spend?\n"))
options = int(input("Where would you like to go?\n 1. Hot Dog Heaven\n 2. Hawkers\n 3. Black Bean Deli\n"))
print(options)

# set total to a value.. budget + 1 = set greater to ensure the total matches the value
# WHILE budget is greater than total
# Where are you eating? Options listed below (NUMBER BETWEEN 1 - 3)
# IF NUM == 1 print() out 2 food items,
# ask which food you want 
# if it is food item1
    #set price equal to a number 

# How many would you like to buy
# if that price is less than or equal to your budget
    #you have found a place to eat 
#otherwise
    #you need to try again

# Option 1 - Hot Dog Heaven 
option1 = ("You chose option 1 (Hot Dog Heaven) \nThey sell the following food items:\n")
opt1_items = ("\t1. Chicago Hot Dog - $4.50\n \t2. Fries - $2.75\n")
prompt1 = int(input(option1 + opt1_items + "What would you you like to buy?\n"))

# Option 2 - Hawkers 
option2 = ("You chose option 2 (Hawkers)\n They sell the following food items:\n\n")
opt2_items = ("\t1. Yi-Yi's Chicken Dumplings - $10.00 \n \t2.Roti Canai - $9.00\n\n")
prompt2 = option2 + opt2_items + "What would you you like to buy?\n"

# Option 3 - Black Bean Deli
option3 = ("You chose option 3 (Black Bean Deli)\n They sell the following food items:\n")
opt3_items = ("\t1. Dark Chicken Platter - $14.60 \n \t2.Yuca Fries - $7.85 ")
prompt3 = option3 + opt3_items + "What would you you like to buy?\n"

# How many of each food item you want?
food_count = int(input("How many would you like to buy?\n"))
total = budget + 1
if(options == 1):
    print(prompt1)
elif(prompt1 == 1 and prompt1 == 2):
    print("How many would you like to buy?\n")
if(prompt1 == 1):
   summary = 4.50 * food_count
   summary = f"That would cost ${summary}"
   print(summary)
elif(prompt1 == 2):
    summary =  2.75 * food_count
    print(summary)




# elif(options == 2):
    # print(prompt2)
# elif(options == 3):
   #  print(prompt3)
#while(budget > total )

# Food items 












