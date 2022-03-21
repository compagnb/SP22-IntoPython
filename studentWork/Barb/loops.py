# Loops
# while(condition):
#   do something

import turtle
#we just imported the turtle library

mike = turtle.Turtle()
ralph = turtle.Turtle()
leo = turtle.Turtle()
don = turtle.Turtle()
#created an instance of the turtle library's class turtle
#it will let us DRAW using mike!!

mike.color("orange")
ralph.color("red")
leo.color("blue")
don.color("purple")
#we can change mikes color!

mike.shape("turtle")
ralph.shape("turtle")
leo.shape("turtle")
don.shape("turtle")
#we can change mikes shape to a turtle, square, circle, triangle

mike.forward(100)
ralph.left(90)
leo.right(90)
don.left(180)

#moves mike forward 100 pixels

mike.forward(90)
ralph.forward(100)
leo.forward(100)
don.forward(100)
#rotates mike right 90 degrees

numb = 10

while True:
## forever loop
    mike.forward(10 + numb)
    mike.left(30)
    numb = numb + 10
    ralph.left(75)
    ralph.forward(45)
    leo.right(90)
    leo.forward(45)
    don.left(45)
    don.forward(45)




    
