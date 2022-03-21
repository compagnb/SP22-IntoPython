# if statements
# if (condition)
#   do something

kai = 0
lola = 300
dallis = 600
matt= 700
jamil = 0
altair = 0
declan = 400
ian = 800
vincent = 900
matthew = 0
barb = 0
addMore = "1"

while (addMore == "1"):
    name = input (" What is your name").lower()
    pointsAdded = input (" How many extra points do you want?")

    if (name == "vincent"):
        vincent = vincent + int(pointsAdded)
        print(vincent)
    elif (name == "declan"):
        declan = declan + int(pointsAdded)
        print(declan)
    elif (name == "dallis"):
        dallis = dallis + int(pointsAdded)
        print(dallis)
    elif (name == "kai"):
        kai = kai + int(pointsAdded)
        print(kai)
    elif (name == "lola"):
        lola = lola + int(pointsAdded)
        print (lola)
    elif (name == "matt"):
        matt = matt + int(pointsAdded)
        print(matthew)
    elif (name == "jamil"):
        jamil = jamil + int(pointsAdded)
        print(jamil)
    elif (name == "altair"):
        altair = altair + int(pointsAdded)
        print(altair)
    elif (name == "declan"):
          matthew = matthew + int(pointsAdded)
          print(matthew)
    elif (name == "ian"):
        ian = ian + int(pointsAdded)
        print (ian)
    elif ( name == "matthew"):
        matthew = matthew + int(pointsAdded)
        print(matthew)
    else:
        barb = barb + int(pointsAdded)
        print(barb)
    addMore= input("Would you like to add points to another person? 1 is yes. 0 is no.")
