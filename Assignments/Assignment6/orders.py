# Yvonne Aime
# COP2500C
# July 21 2023
# Assignment 6: Taking Orders

# menu_shortener() - Function
def menu_shortener(meal):
    # Formats words to all upper case 
    meal = meal.upper()
    # Split the item into words(based on spacing)
    wordcheck = meal.split()
    # Checks if it is 2-3 words 
    if(len(wordcheck)== 2 or len(wordcheck)== 3):        
        # Empty list, to append new words/abbreviations
        wordcheck02 = []
        for i in range(len(wordcheck)):
            new = wordcheck[i]
            #Appends new words 
            wordcheck02.append(new[0])
        # Rejoins words after split
        combine = "".join(wordcheck02)  
    # Checks if it is more 3 or more words 
    elif(len(wordcheck)>3 or len(wordcheck) <2):
        combine = meal[:3]
    return combine

# Main function  
def main():
    # Asks user 'how many items' and is stored in 'orders' variable
    orders = int(input("How many items would you like to order?\n"))
    # Initializes 'meal' variable within for loop 
    item_list = []
    new_list = []
    for i in range(orders):
            meal = (input("What is item #"+ str(i+1)+ "?\n"))
            new_list.append(meal)
            item_list.append(menu_shortener(meal))
    # Header for final order printout
    print("⋆Your Order: ⋆\n")
    # Separates list with dash - and numbers the items ordered 
    for i in range(len(item_list)):
        print(str(i+1) + "." + item_list[i] + "-" + new_list[i])
    # Prints out and returns final items
    return new_list

main()