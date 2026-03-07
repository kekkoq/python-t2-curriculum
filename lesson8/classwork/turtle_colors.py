import turtle

t = turtle.Turtle()
t.speed(6)

t.color("pink")
t.forward(75)
t.pensize(10)
t.forward(75)


#filling shapes
t.penup()
t.goto(-150, 0)
t.pendown()

t.color("green")
t.begin_fill()
for i in range(4):
  t.forward(100)
  t.left(90)
  
t.end_fill()

turtle.done
