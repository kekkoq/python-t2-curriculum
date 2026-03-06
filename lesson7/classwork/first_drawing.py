import turtle

t = turtle.Turtle()
t.speed(5)

for i in range(4): #this is a loop
    t.forward(100)
    t.left(90)

t.penup()
t.goto(-150, 0) #teleport to a space on the snake looking thingy
t.pendown()


for i in range(3):
    t.forward(100)
    t.left(120)
t.penup()
t.goto(-225, 0)
t.pendown()
t.circle(50) # 50 = the radius
t.penup()

t.goto(0, 200)
t.pendown()

for i in range(4):
    t.forward(80)
    t.left(90)

t.goto(0, 280)
t.left(90)

t.right(90)
for i in range(3):
    t.forward(80)
    t.left(120)
turtle.done()