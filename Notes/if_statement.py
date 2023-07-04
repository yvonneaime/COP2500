# If Statemnet Notes

grade = float(input("What precentage do you have in this class?\n"))

# Logical Operators
    # < - less than
    # > - greater than
    # <= - less than or equal to 
    # >= - greater than or equal to 
    # == - equal
    # != - not equal 

    # AND - both statements have to be true
    # OR
    # NOT

# If we get a 90 or above = A
if (grade >= 90):
    print("You got an A!")
    print("Yay! Good 4 You! ")

if (grade >= 80 and grade < 90):
    print("You got an B!")
    
print("Program End")

# ELSE IF Statement
if (grade >= 90):
    print("A")
elif (grade >= 80):
    print("B")
elif (grade >= 70):
    print("C")
# ELSE Statement
else:
    print("F")


