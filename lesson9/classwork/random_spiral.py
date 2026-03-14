import turtle

t = turtle.Turtle()

t.speed(6)
t.width(2)

# def draw_triangle(length, color):
#   t.pencolor(color)
#   for i in range(3):
#     t.forward(length)
#     t.left(120)
    
# colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# size = 4

# for i in range(30):
#   draw_triangle(size, colors[i % 6])
#   t.left(10)
#   t.forward(3)
#   size = size + 3
  
def draw_spiral(colors, turns, step, angle):
  for i in range(turns):
    t.pencolor(colors[i % len(colors)])
    t.width(1 + i // 50)
    t.forward(i * step)
    t.left(angle)
    
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
draw_spiral(colors, 220, 1.1, 59
