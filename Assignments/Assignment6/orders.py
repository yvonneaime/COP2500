# Yvonne Aime
# COP2500C
# July 21 2023

# Assignment 6: Taking Orders

# Main function - 
def main():
  
    # Asks user 'how many items' and is stored in 'orders' variable
    orders = int(input("How many items would you like to order?\n"))

        # Initializes 'items' variable within for loop 
    item_list = []

    for i in range(orders):
            item = (input("What is item #"+ str(i+1)+ "?\n"))
            item_list.append(item)


    # Checks to see how long the list is 
    length = len(item_list)

    print("Your Order:\n")

    # Separates lists with dash - 
    for index in range(length):
        print(index, "-" , item_list[index])
    # Prints final items
    return item_list


# 'ordered_items' variable stores main () function   
ordered_items = main()

# menu_shortener() - Function
def menu_shortener(item):
    item = ""
    # Split the item into words
    words = item.split()
    
    if len(words) in (2, 3):
        # If 2-3 words in input, take the first letter of each word and capitalize the code
        words = words.capitalize()
        print(words, "-", words)
        #If there are more than three words or only one word
    #get the first three letters of the first word
    #Capitalize the code
    # Example: "Bacon Lettuce Tomato Egg Turkey" becomes BAC
    # Example: "Sandwich" becomes SAN
    #if len(words==1 )