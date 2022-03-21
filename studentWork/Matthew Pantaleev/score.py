#if statements
#if (condition)
#   do something
#else
#   do something

kai = 0
lola = 300
dallis = 600
matthew = 700
jamil = 0
altair = 0
declan = 400
andy = 1000
ian = 800
vincent = 900

name = input("enter your name.")
pointsadded = input("please enter the number of points you would like to add.")

if(name == "vincent"):
    vincent = vincent + int(pointsadded)
    print(vincent)

elif(name == "matthew"):
    matthew = matthew + int(pointsadded)
    print (matthew)
