import turtle as trtl

#create a turtle object
painter = trtl.Turtle()

def draw_circle(radius, color):
    painter.begin_fill()
    painter.color(color)
    painter.circle(radius)
    painter.end_fill()

# first circle
draw_circle(100, "blue")

# second circle
painter.penup()
painter.forward(200)
painter.pendown()
draw_circle(100, "red")

#set the windows settings
wn = trtl.Screen()
wn.mainloop()