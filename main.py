#   a114_guess.py
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.penup()
painter.color("salmon")
painter.pensize(2)

spiral_space = 0

while (spiral_space < 70): 
  painter.color("orange")
  painter.goto(0,0)
  painter.right(20)
  painter.forward(60+(spiral_space*3))
  if (spiral_space % 5 == 0):
    painter.color("navy")
  if (spiral_space % 10 == 0):
    painter.color("green")
  painter.pendown()
  painter.circle(10)
  painter.penup()
  spiral_space = spiral_space + 1


wn = trtl.Screen()
wn.mainloop()