# Yvonne Aime
# COP2500C 
# Assignment 7 - Full Menu Please 
# July 25 2023


# get_menu Function:
from fileinput import filename


def get_menu(filename):
    # Empty Dictionary
    menu = {}
    # Opens the file
    file_open = open(filename,"r")
    fname = filename
    file_num = int(file_open.readline())
    food_items = 0
    all = 0 

    for i in range(file_num):
        # Setting 'open(filename)' to a new variable
        new_open = file_open.readline()
        print(new_open)
        # Splits the food items and prices 
        all = float(all)
        food_items = str(food_items)
        # Splits values 
        split_file = new_open.split()
        menu[split_file[0].title()] = float(split_file[1])

        return menu
   
# print_receipt Function:
def print_receipt(food_items, all):
    file_open = open(filename,"r")

# file input and output is NOT in main()
def main():
    main_menu = []
    # Asks user for file name 
    filename = input("What menu would you like to load?\n")
    filename = filename.lower()
    new_menu = get_menu(filename)
    request = 0 
    while(request != "end"):
        # Asks user what they want to order
        request = input("What would you like to order?\n")
        request = request.lower()
        if request in new_menu:
            print("Its been added!")
        elif(request=="end"):
            print("Goodbye")
        else:
            print("We do not have that.")
main()
