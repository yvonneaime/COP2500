# Yvonne Aime
# COP2500
# July 18 2023

# Assignment 5: Restaurant Icons

# The position will be two different variables.  (X, Y, Size)
# The size of the icon will change based on the size variable
# The X and Y is the starting position of the turtle

import turtle 

# Design 1 Function
def draw_flower(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.color("#00ffb3")
    turtle.pensize(10)
    
    turtle.setheading(0)

    turtle.fillcolor("#94ED64")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

    turtle.left(90)
    turtle.color("#D70143")
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(-size/2, 90)
    turtle.end_fill()

    for i in range(5):
            turtle.forward(size/4)
            turtle.right(180)
    else:
        turtle.penup()
        turtle.forward(size/8)
        turtle.pendown()
        for i in range(5):
            turtle.circle(size/16)
            turtle.left(72)
   

# Design 2 Function
def draw_flower02(x,y, size, color):
    turtle.fillcolor(color)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(size/8)
    for i in range (4):
        turtle.forward(200)
        turtle.right(90)
    turtle.left(90)
    turtle.circle(-100,180)


# Main Function
def main():
    draw_flower(0, 200, 200, "#104fc4")
    draw_flower(-150, 300, 100, "#104fc4")
    draw_flower(0, -300,-150, "#104fc4")
main()