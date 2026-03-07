import turtle

t = turtle.Turtle()
t.speed(3)

t.forward(100)

t.penup()
t.goto(-100, 0)
t.pendown()

t.circle(40)

t.penup()
t.goto(0, 100)
t.pendown()

t.shape("turtle")
t.begin_fill()
t.color("blue")
for i in range(6):
  t.color("blue")
  t.forward(50)
  t.left(60)
t.end_fill()
  
t.color("green")
t.penup()
for i in range(6):
  t.pendown()
  t.stamp()
  t.penup()
  t.forward(50)
  t.left(60)
t.stamp()
