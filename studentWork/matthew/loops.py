


# Loops
# while(condition):
#    do something

import turtle
#we just imported the turtle library

mike = turtle.Turtle()

ralph = turtle.Turtle()
#created an instance of the turtle library's class turtle
#it will let us DRAW using mike!!

#it will let us DRAW using ralph!!

mike.color("purple")

ralph.color("orange")
#we can change mikes color!

#we can change ralph color!

mike.shape("turtle")

ralph.shape("turtle")
#we can change mikes shape to a turtle, circle, triangle

#we can change ralph shape to a turtle, circle, triangle 

mike.forward(260)

ralph.behind(300)
#moves mike forward 260 pixels



numb = 75

numb = 80

mike.right(109)

ralph.left(180)
#rotate mike right 87 degrees

#rotate ralph left 58 degrees

while True:
## forever loop
    mike.forward(48)
    mike.left(30)
    numb = numb + 10
    
    ralph.forward(87)
    ralph.right(78)
    numb = numb + 10
