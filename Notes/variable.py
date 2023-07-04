#Variable Notes
# COP 2500C
# June 28, 2023

# one equal sign =, is read as "set to/ save to", always goes from right to left
# Read this as save '5' to x 
# x = 5

# Use meaningful names
age = 19
print(age)
print("You were", age, "years old.")

# Get current age and add 1 to it and save it as 'age'
age = age + 1 
print("You are", age, "years old.")

# ** - Exponents 
# Ex: 5 ** 2 = 25, 5^2 same thing

# *
# /
# // - integer division/ floor division (Always rounds down--to the floor)
# % - modulos (Remainder)
example1= 7 % 3
print(example1)

example2= 7 // 3
print(example2)

# Data types (Four TYPES)
    # integer - int (whole number)
    # float - float (decimal)
    # boolean - True/False
    # strings - str - A combination of letters, numbers, and symbols

# Input
age = int(input("How old are you?\n"))
print("You are currently", age, "years old.")


future_age = age + 10
print("In ten years you will be", future_age, "years old." )

