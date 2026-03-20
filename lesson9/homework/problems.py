# Problem 1
# Write a function draw_star(size) that draws a 5-point star using turtle.
# Call it.
import turtle
t = turtle.Turtle()

t.speed(6)
t.width(2)

def draw_star(size):
    for i in range(5):
        t.forward(size)
        t.right(144)

draw_star(100)

turtle.done()

# Problem 2
# Use a loop to draw 20 circles.
# Each time, move forward a little and change color.
import turtle
t = turtle.Turtle()

t.speed(6)
t.width(2)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

t.penup()
t.goto(-200, 0)

for i in range(20):
    t.pendown()
    t.pencolor(colors[i % len(colors)])
    t.circle(10)
    t.penup()
    t.forward(20)
turtle.done()

# Problem 3
# Draw the word "SOVA" in block letters using turtle lines.
# (It does not have to be perfect.)
t.penup()
t.goto(-150, 50)
t.pendown()

t.forward(50)
t.backward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)

t.penup()
t.goto(-75, 50)
t.right(270)
t.pendown()

t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)

t.penup()
t.backward(75)
t.right(250)
t.pendown()

t.forward(115)
t.left(135)
t.forward(115)

t.penup()
t.goto(125, 50)
t.right(155)
t.pendown()

t.forward(100)
t.backward(100)
t.left(90)
t.forward(50)
t.right(90)
t.forward(100)
t.backward(50)
t.right(90)
t.forward(50)

turtle.done()


# Problem 4
# Create a random art generator:
# - Pick random colors
# - Draw random shapes
# - Use at least 30 shapes
import turtle
import random

t = turtle.Turtle()
t.speed(6)
t.width(2)

colors = ["red", "blue", "green"]

def draw_circle(size):
    t.circle(size)

def draw_square(size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

def draw_triangle(size):
    for _ in range(3):
        t.forward(size)
        t.left(120)

shapes = [draw_circle, draw_square, draw_triangle]

t.penup()


for i in range(1):
    t.pendown()

    t.color(random.choice(colors))

    shape = random.choice(shapes)
    shape(10)

    t.penup()
    t.forward(40)
turtle.done()

# Problem 5
# Make your own mini-project drawing and add a short comment explaining what it is.

# I made a simple little square house with a door.

for i in range(4):
  t.forward(100)
  t.right(90)


t.left(45)
t.forward(70)
t.right(90)
t.forward(75)

t.penup()
t.right(45)
t.forward(100)
t.right(90)
t.forward(40)
t.right(90)

t.pendown()
t.forward(50)
t.left(90)
t.forward(25)
t.left(90)
t.forward(50)
