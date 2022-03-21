kai = 0
lola = 300
dallas = 600
matthew = 700
Jamil = 0
altair = 500
declan = 400
andy = 1000
ian = 800
vincent = 900
matt = 0
barb = 0
addMore = "1"
while(addMore == "1"):
    name = input ("please enter your name.")
    print (name)
    pointsAdded = input ("please enter the number of points you would like to add.")


    if(name.lower() == "vincent") :
        vincent = vincent + int(pointsAdded)
        print(vincent)
    elif(name.lower() == "declan"):
        declan = declan + int(pointsAdded)
        print(declan)
    elif(name.lower() == "jamil"):
        jamil = jamil + int(pointsAdded)
        print(jamil)
    elif(name.lower() == "altair"):
        altair = altair  + int(pointsAdded)
        print(altair)
    elif(name.lower() == "andy"):
        andy = andy + int(pointsAdded)
        print(andy)
    elif(name.lower() == "ian"):
        ian = ian  + int(pointsAdded)
        print(ian)
    elif(name.lower() == "matthew"):
        matthew = matthew + int(pointsAdded)
        print(matthew)
    elif(name.lower() == "dallas"):
        dallas = dallas  + int(pointsAdded)
        print(dallas)
    elif(name.lower() == "lola"):
        lola = lola  + int(pointsAdded)
        print(lola)
    elif(name.lower() == "kai"):
        kai = kai  + int(pointsAdded)
        print(kai)
    elif(name.lower() == "matt"):
        matt = matt  + int(pointsAdded)
        print(matt)
    else:
        barb = barb + int(pointsAdded)
        print(barb)
        input("would you like to add more points")
        addMore = input("Do you want to add points to another person type 1 for yes and 0 for no")

