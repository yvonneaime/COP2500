# Lab 1 - Challenge 3
# Yvonne Aime, COP2500, July 4 2023

import math

# Headings 
attend = int(input("How long have you attended UCF\n"))

fave_ice = str(input("What is your favorite ice cream?\n"))

name = str(input("What is your name?\n"))
 
# Total price = The years attended * $5
reg_price = (attend*5)

# 50% off for 'mint' icecream
if (fave_ice == "mint"):
    reg_price = math.floor(reg_price / 2) 

# Knightro pays $1000 regardless of given info
if (name.lower() == "knightro"):
    reg_price = 1000


# Prints out the Final/Total Cost
print(f"Your ice cream costs: ${reg_price}")
