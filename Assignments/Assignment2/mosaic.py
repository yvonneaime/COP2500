# Assignment 2 - Food Mosaic
# Yvonne Aime, COP2500, July 4 2023

# Turtle is referenced as 't'
import turtle as t 
import math

# Sets the screen object as scr 
scr=t.getscreen()

# Sets the background color
scr.bgcolor("white")

t.shape("turtle")
t.color("blue")

# Drawing the bun front facing
t.pencolor("tan")
t.color("tan")
t.pensize(3)
t.penup()
t.setheading(0)
t.begin_fill()
t.circle(35,190)
t.pendown()
t.circle(45,170)
t.goto(45,120)
t.penup()
t.begin_fill()
t.left(60)
t.circle(35,170)
t.pendown()
t.end_fill()

t.exitonclick()