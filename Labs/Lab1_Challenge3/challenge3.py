# Lab 1 - Challenge 3
# Yvonne Aime, COP2500, July 4 2023


attend = int(input("How long have you attended UCF\n"))

fave_ice = str(input("What is your favorite ice cream?\n"))

name= str(input("What is your name?\n"))

print("Your ice cream costs: $\n")

reg_price = (attend*5)
if (fave_ice == "mint"):
    reg_price = reg_price / 2 
    
 # Prints out all headings
print(attend,fave_ice,name)