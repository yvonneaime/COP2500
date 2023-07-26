# Yvonne Aime
# COP2500C 
# Assignment 7 - Full Menu Please 
# July 25 2023


# get_menu Function:
def get_menu(filename):
    # Empty Dictionary
    menu = {}
    # Opens the file
    file_open = open(filename,"r")
    fname = filename
    file_num = int(file_open.readline())
    food_items = 0
    all = 0 

    for i in range(food_items):
        # Setting 'open(filename)' to a new variable
        new_open = file_open.readline()
        print(new_open)
        # Splits the food items and prices 
        all = float(all)
        item = str(item)
        # Splits values 
        split_file = new_open.split()
        menu[split_file[0].capitalize()]=float(split_file[1])
        return menu
   
# print_receipt Function:
def print_receipt():
    file_open=open(filename,"r")

# file input and output is NOT in main()
def main():
    main_menu = []
    # Asks user for file name 
    filename = input("What menu would you like to load?\n")
    filename = filename.lower()
    new_menu = get_menu(filename)
    request = 0 
    while(request != "end" or "End"):
        # Asks user what they want to order
        request = ("What would you like to order?\n")
main()
