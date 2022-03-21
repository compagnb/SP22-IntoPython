# Loops
# while(condition)
#   do something

import turtle
#we just imported the turtle library

mike = turtle.Turtle()
#created an instance of the turtle library's class turtle
#it will let us DRAW using mike!

mike.color ("orange")
# we can change mikes color!
mike.shape("turtle")
mike.forward(100)
mike.right(90)

while True:
    mike.forward(100 + 1)
    mike.left (30)
    numb = numb + 10
