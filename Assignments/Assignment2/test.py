
import turtle

# Turtle is referenced as 't'
t = turtle.Turtle()

# Sets the screen object as 'screen'
screen = turtle.Screen()

# Sets background color
screen.bgcolor("#80CCF0")

# Starts off drawing
t.speed(3)
t.penup()
t.goto(0,-200)
t.pendown()
t.right(90)

# Draw the hotdog buns
t.penup()
t.left(11)
t.color('#C79450')
t.begin_fill()
t.circle(65, 180)
t.forward(300)
t.circle(65, 180)
t.forward(300)
t.end_fill()
t.pendown()

# Draws hot dog (frankfurter)
t.penup()
t.color('#d62929')
t.right(10)
t.begin_fill()
t.circle(30, 180)
t.forward(365)
t.circle(30, 180)
t.forward(365)
t.end_fill()
t.pendown()


# Mustard on hot dog
t.pensize(11)
t.pencolor('yellow')
t.penup()
t.goto(35, 160)
t.pendown()

t.penup()
t.begin_fill()
t.color('yellow')
t.pendown()
t.forward(100)
t.left(-30)
t.end_fill()

t.begin_fill()
t.color('yellow')
t.forward(60)
t.left(50)
t.end_fill()


t.begin_fill()
t.forward(60)
t.end_fill()
t.right(20)
t.forward(40)
t.left(30)
t.forward(40)
t.right(10)
t.forward(10)
t.right(50)
t.forward(75)

# Exits program
turtle.done()