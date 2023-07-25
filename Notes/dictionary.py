# Yvonne Aime
# COP2500C
# July 24 2023
# Dictionary Notes 


# Dictionary simialr to a list
# Require a key and a value
# Values do not need to be unique 
# Instead of an integer value, you use a string 
# copy(), keys(), and pop() 

# To create an empty dictionary:
students = {}

# If you want to create a dictionary with different words inside:
# Keys = their names 
students = {"Kal": 92, "David": 90, "Jen":85 }
print(students)

name = input("What is their name?\n")
grade = input("What is their grade?\n")

# To add a new person to the list, put the key in the bracket and set the value
students[name] = grade
students["Kyle"] = 100

print(students)

# Prints Miguel's grade
if "Miguel" in students:
    print(students["Miguel"])


# How to change value
students["Miguel"] = students["Miguel"]/ 2 + 3 
print(students)

# How to remove items from a dictionary
students.pop("Miguel")
print(students)



total = 0
# Will go through each key in the dictionary and save it as a variable key
for key in students:
    print(key, "Value", students[key])
    total += students[key]

average = total / len(students)
print(average)
