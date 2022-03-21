#if statements
#if(condition)
#   do something
#else
#   do something

kai = 0
lola = 300
dallis = 1100
matthew = 950
jamil = 0
altair = 500
declan = 1400
andy = 2000
ian = 800
vincent = 1400
matt = 0
barb = 0
addMore = "1"

while(addMore == "1"):
    name = input("please enter your name.").lower()
    print(name)
    pointsAdded = input("please enter the number of points you would like to add.")

    if(name == "vincent"):
        vincent = vincent + int(pointsAdded)
        print(vincent)
    elif(name == "declan"):
        declan = declan + int(pointsAdded)
        print(declan)
    elif(name == "lola"):
        lola = lola + int(pointsAdded)
        print(lola)
    elif(name == "kai"):
        kai = kai + int(pointsAdded)
        print(kai)
    elif(name == "dallis"):
        dallis = dallis + int(pointsAdded)
        print(dallis)
    elif(name == "matthew"):
        matthew = matthew + int(pointsAdded)
        print(matthew)
    elif(name == "jamil"):
        jamil = jamil + int(pointsAdded)
        print(jamil)
    elif(name == "altair"):
        altair = altair + int(pointsAdded)
        print(altair)
    elif(name == "andy"):
        andy = andy + int(pointsAdded)
        print(andy)
    elif(name == "ian"):
        ian = ian + int(pointsAdded)
        print(ian)
    elif(name == "matt"):
        matt = matt + int(pointsAdded)
        print(matt)
    else:
        barb = barb + int(pointsAdded)
        print(barb)

    addMore = input("Do you want to add points to another person? Type 1 for yes and 0 for no.")


    


    















