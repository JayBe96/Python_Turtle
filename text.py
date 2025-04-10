import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Example Text on Turtle Graphics")
screen.setup(width=800, height=600)
screen.bgcolor("black")

# Create a turtle named 'writer'
writer = turtle.Turtle()
writer.speed(1)  # Set the writing speed

# Function to write text
def write_text(text, x, y, color, size):
    writer.penup()  # Don't draw when moving to start position
    writer.goto(x, y)  # Move to the specified position
    writer.pendown()  # Start drawing
    writer.color(color)  # Set text color
    writer.write(text, font=("Arial", size, "normal"))  # Write text


write_text("Shaco", -50, 0, "cyan", 36)
write_text("Jay", -30, -50, "magenta", 36)

# Hides the turtle (Arrow / Cursor)
writer.hideturtle()

# Needed to keep the window open
turtle.done()
