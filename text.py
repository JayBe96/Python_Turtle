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
def write_text(text:str, x:float, y:float, color:str, size:int):
    """
    Writes text on the screen at a specified position with a given color and size.
    Parameters:
        text (str): The text to be written.
        x (float): The x-coordinate of the text's position.
        y (float): The y-coordinate of the text's position.
        color (str): The color of the text (e.g., "red", "blue").
        size (int): The font size of the text.
    """
    writer.penup()  
    writer.goto(x, y)  
    writer.pendown()  
    writer.color(color)  
    writer.write(text, font=("Arial", size, "normal"))  


write_text("Shaco", -50, 0, "cyan", 36)
write_text("Jay", -30, -50, "magenta", 36)

# Hides the turtle (Arrow / Cursor)
writer.hideturtle()

# Needed to keep the window open
turtle.done()
