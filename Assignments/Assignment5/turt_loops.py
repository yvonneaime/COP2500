
import turtle, random

def draw_house():
    turtle.setheading(0)
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.left(90)
    
def draw_better_house(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    turtle.setheading(0)
    for i in range(4):
        turtle.forward(200)
        turtle.right(90)
    turtle.left(90)
    turtle.circle(-100, 180)


def draw_bigger_house(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    turtle.setheading(0)
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.left(90)
    turtle.circle(-size/2, 180)

def draw_colorful_house(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.color("#00ffb3")
    turtle.pensize(10)
    
    turtle.setheading(0)

    turtle.fillcolor("#09b380")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

    turtle.left(90)
    turtle.color("#000000")
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(-size/2, 180)
    turtle.end_fill()

    turtle.color("#FFFF00")
    turtle.penup()
    turtle.right(90)
    turtle.forward(size/2)
    turtle.right(90)
    turtle.forward(size/8)
    turtle.pendown()

    
            

def main():
    draw_colorful_house(200, 200, 300, "#104fc4")
    draw_colorful_house(-200, 100, 200, "#ff00d4")
    draw_colorful_house(-300, -100, 50, "#59ff00")
main()

