from turtle import *

# Set up the screen
screen = Screen()
screen.title("Example Colors on Turtle Graphics")
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

colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "cyan", 
            "magenta", "lime", "brown", "white", "gray", "gold", "violet", "indigo"]

x, y = -100, -100
for i in range(16):
    draw_circle(x, y, colors[i % len(colors)])
    x += 50
    if (i + 1) % 4 == 0:  # Move to the next row after 4 circles
        x = -100
        y += 50


done()