## Problem 1
# Use turtle to draw a filled square inside a larger square.
import turtle
t = turtle.Turtle()
t.speed(6)

t.begin_fill()
for i in range(4):
  t.forward(100)
  t.left(90)
  
t.end_fill()

t.penup()
t.backward(50)
t.right(90)
t.forward(50)
t.left(90)
t.pendown()

for i in range(4):
  t.forward(200)
  t.left(90)
turtle.done()
# Problem 2
# Use turtle to draw a flower with 6 petals.
# Each petal can be made using a small circle arc.
t = turtle.Turtle()
t.speed(6)

for i in range(6):
    t.circle(60, 60)
    t.left(120)
    t.circle(60, 60)
    t.left(60)

turtle.done()


# Problem 3
# Use turtle to draw a rainbow:
# Draw 5 semicircles with different colors, each one bigger than the last.
import turtle

t = turtle.Turtle()
t.speed(6)
t.width(10)

colors = ["blue", "green", "yellow", "orange", "red"]
radius = 100

for color in colors:
    t.color(color)
    t.penup()
    t.goto(0, -radius)   
    t.setheading(0)      
    t.pendown()
    t.circle(radius, 180)
    radius += 20         

turtle.done()


# Problem 4
# Use turtle to draw a grid of 3x3 small squares.
t = turtle.Turtle()
t.speed(5)

def square(size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

size = 50   

for row in range(3):          
    for col in range(3):      
        square(size)
        t.penup()
        t.forward(size)       
        t.pendown()
    
    t.penup()
    t.backward(size * 3)
    t.right(90)
    t.forward(size)          
    t.left(90)
    t.pendown()

turtle.done()


# Problem 5
# Use turtle to make a simple "logo" using at least 3 different colors and 2 shapes.
import turtle

t = turtle.Turtle()
t.speed(6)
t.width(3)

t.color("blue", "lightblue")
t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.goto(0, 0)
t.setheading(90)
t.forward(60)
t.setheading(210)
t.pendown()

t.color("yellow", "gold")
t.begin_fill()
for _ in range(3):
    t.forward(120)
    t.left(120)
t.end_fill()

t.penup()
t.goto(-80, 0)
t.setheading(0)
t.pendown()

t.color("red", "salmon")
t.begin_fill()
for _ in range(2):
    t.forward(160)
    t.right(90)
    t.forward(30)
    t.right(90)
t.end_fill()

turtle.done()
