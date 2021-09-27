import turtle as trtl

#create a turtle object
painter = trtl.Turtle()

# first circle
painter.begin_fill()
painter.color("blue")

painter.circle(100)
painter.end_fill()

#set the windows settings
wn = trtl.Screen()
wn.mainloop()