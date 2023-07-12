# Yvonne Aime, COP2500, July 12 2023
# Lists 

def main():
    # Define alist
    shopping = []

    # Add things to a list..
    # Append - add things to end of list
    shopping.append("Cookies")
    shopping.append("Juice")
    shopping.append("Melk")

    # Add items in a location
    shopping.insert(1, "Chips & Guac")

    shopping.append("Mangos")
    shopping.insert(1, "Mangos")

    print(shopping)

    # Delete items out of list
    
    # Delete items based on value (one value - at 1 )
    shopping.remove("Mangos")

    # Delete items based on position
    shopping.pop(4)
    print(shopping)


    for i in range(50):
        shopping.append("Mangos")
    
    print(shopping)

    # How to delete ALL Mangos
    while("Mangos" in shopping):
        shopping.remove("Mangos")
  
    print(shopping)

    # This checks to see if apples is on the list
    if("Apples" in shopping):
        shopping.remove("Apples")
    else:
        print("NO Apples Silly!")

    # See how long a list is (How many items are in it)
    length = len(shopping)
    print(length)

    # Accessing the list's values
    print(shopping[3])
    # Negative Value starts from the right of the list
    print(shopping[-2])

    # Iterate over a list -- FOR IN 
    for index in range(length):
        print(index, "-" , shopping[index])

    # For each loop
    for item in shopping:
        print("Item", item)

    # How to change one item in the list
    shopping[0] = "Cake"
    print(shopping)

    # Adds -"ay" to ending of each item on list
    for index in range(length):
        shopping[index] = shopping[index]+"ay"
    print(shopping)

    # Sorts list
    shopping.sort()
    print(shopping)

main()