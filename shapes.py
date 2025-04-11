from signal import pause
from turtle import *

# Set up the screen
screen = Screen()
screen.title("Example Shapes on Turtle Graphics")
screen.setup(width=800, height=600)
screen.bgcolor("black")

# Create a turtle
turtle = Turtle()
turtle.speed(1)  # Set the writing speed


# Function to draw a filled circle with 25 radius  
def draw_circle(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(25)  
    turtle.end_fill()

# Function to draw a filled square with 50x50 size
def draw_square(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(50) 
        turtle.right(90)
    turtle.end_fill()

# Function to draw a filled square with 50x50 size
def draw_triangle(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(50) 
        turtle.right(120)
    turtle.end_fill()

draw_circle(0, 0, "white")
draw_square(-50, -50, "white")
draw_triangle(50, 50, "white")

done()