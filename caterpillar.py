import turtle as trtl

#create a turtle object
painter = trtl.Turtle()

# first circle
painter.begin_fill()
painter.color("blue")
painter.circle(100)
painter.end_fill()

# second circle
painter.penup()
painter.forward(200)
painter.pendown()
painter.begin_fill()
painter.color("red")
painter.circle(100)
painter.end_fill()

#set the windows settings
wn = trtl.Screen()
wn.mainloop()