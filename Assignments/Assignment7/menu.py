# Yvonne Aime
# COP2500C 
# Assignment 7 - Full Menu Please 
# July 25 2023

def get_menu(filename):
    # Empty dictionary 
    menu_items = {}
    # Opens file
    open_file = open(filename, "r")
    # Converts to integers
    numbered = int(open_file.readline())
    for i in range(numbered):
        food_items = ()
    return menu_items

def print_receipt(total):
    new_file = open("receipt.txt","w+")
    new_file.write("Receipt:\n")

def main():
    
    new_file.write("Welcome!:\n")
    filename = input("What menu would you like to load?\n")

    pass
main()