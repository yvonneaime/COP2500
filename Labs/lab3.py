# Yvonne Aime
# COP2500
# July 20 2023

# Summer Lab 3: Challenge 3


print("Welcome to the store!")

# initializes list 
options = []
for i in range(5):
    # Stores input in variable - to_eat
    to_eat = input("What would you like for item " + str(i+1)+ "?\n")
    options.append(to_eat.title())
print("You have ordered: ")

# Prints numbered list with user input 
for i in range(5):
    print(str(i+1)+ "." + options[i])