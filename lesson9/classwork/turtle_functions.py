import turtle

t = turtle.Turtle()
t.speed(3)

def draw_triangle(length):
    for i in range(3):
        t.forward(length)
        t.left(120)

t.goto(100, 0)
t.pendown()
draw_triangle(100)
t.penup()

t.goto(0, 0)
t.pendown()
t.color("blue")
draw_triangle(50)
t.penup()

def draw_polygon(sides, length):
    angle = 360 / sides
    for i in range(sides):
        t.forward(length)
        t.left(angle)

t.goto(0, 100)
t.pendown()
t.color("red")
draw_polygon(3, 40)
t.penup()

t.goto(0, 150)
t.pendown()
t.color("green")
draw_polygon(12, 30)
