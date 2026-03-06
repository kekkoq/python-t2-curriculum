# Problem 1
# Use turtle to draw 3 squares in a row.
# Each square should have side length 60.
import turtle

t = turtle.Turtle()
t.speed(5)

for i in range(3):
    for i in range(4):
        t.forward(60)
        t.left(90)
    t.penup()
    t.backward(150)
    t.pendown()

turtle.done()

# Problem 2
# Use turtle to draw a "staircase" with 5 steps.
# Each step goes forward 40, then up 40 (turn left 90), then turn right back.
t = turtle.Turtle()
t.speed(5)

for i in range(5):
    for j in range(1):
        t.forward(40)
        t.left(90)
        t.forward(40)
        t.right(90)

turtle.done()


# Problem 3
# Use turtle to draw a star (5 points).
t = turtle.Turtle()
t.speed(5)

for i in range(5):
    t.forward(50)
    t.left(144)

turtle.done()

# Problem 4
# Use turtle to write your name on the screen using turtle.write().
t = turtle.Turtle()
t.speed(5)

turtle.write("Kaiden")

turtle.done()


# Problem 5
# Use turtle to draw a pattern of 10 circles.
# Move a little each time so the circles do not overlap completely.
t = turtle.Turtle()
t.speed(5)
t.penup()
t.goto (0, 200)
t.left(90)
t.pendown()

for i in range(10):
    t.circle(15)
    t.penup()
    t.backward(50)
    t.pendown()

turtle.done()