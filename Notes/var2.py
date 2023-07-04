# COP 2500C
# June 28, 2023

# Variable Notes

credit = int(input("How many credits do you have?\n"))
gpa = float(input("What is your current GPA?\n"))
grade = int(input("What grade did you get as an integer\n"))

points = credit * gpa
print("You have,", points, "points")

new_points = 3 * grade
points = points + new_points

gpa = points / (4)
print("Your gpa is", gpa)

# How can we format our output?
# %f in the quotes is a placeholder for a floating point number 
#  %3f- Limits to the first 3 numbers after the decimal point 
print("Your gpa is %3f" % gpa)
