# Yvonne Aime
# COP2500
# July 19 2023

# Turtle with Functions and Loops

import turtle

def draw_house():
    #
    turtle.setheading(0)
    for i in range(4):
          turtle.forward(200)
          turtle.right(90)
    turtle.left(90)
    turtle.circle(-100,180)

def draw_better_house(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.setheading(0)
    for i in range (4):
        turtle.forward(200)
        turtle.right(90)
    turtle.left(90)
    turtle.circle(-100,180)

def draw_bigger_house(x,y, size):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.setheading(0)
    for i in range (4):
        turtle.forward(200)
        turtle.right(90)
    turtle.left(90)
    turtle.circle(-100,180)

def colorful_house(x,y, size, color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color("green")
    turtle.fillcolor("blue")

    
fur 
def main():
    draw_house()
    draw_better_house(-500,0)
    draw_better_house(-250,0)
    draw_better_house(-500,0)

main()
