import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightgray")

# Create the turtle object
spinner = turtle.Turtle()
spinner.shape("arrow")
spinner.color("black")
spinner.speed(0)
spinner.penup()

# Define the wheel sections
sections = ["Prize 1", "Prize 2", "Prize 3", "Prize 4", "Prize 5"]
colors = ["red", "green", "blue", "yellow", "purple"]
angle = 360 / len(sections)

# Draw the wheel
for i in range(len(sections)):
    spinner.fillcolor(colors[i])
    spinner.begin_fill()
    spinner.circle(100, angle)
    spinner.left(angle)
    spinner.end_fill()

# Spin the wheel
def spin_wheel():
    spinner.right(random.randint(1, 360 * 5))  # Spin the wheel randomly

# Bind the spin function to a key press
screen.onkey(spin_wheel, "space")
screen.listen()

turtle.done()
