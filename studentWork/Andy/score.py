#if statements
#if(condition)
#   do something
#else
#   do something

kai = 0
lola = 300
dallis = 600
matt = 700
jamil = 0
altair = 500
declan = 400
andy = 1000
ian = 800
vincent = 900
matthew = 0
barb = 0

name = input("Enter your name.").lower()
pointsAdded = input("Enter the munber of points you want to add.")

if(name == "vincent"):
    vincent = vincent + int(pointsAdded)
    print(vincent)
else:
    if(name == "andy"):
        andy = andy + int(pointsAdded)
        print(andy)
    else:
        if(name == "ian"):
            ian = ian + int(pointsAdded)
            print(ian)
        else:
            if(name == "declan"):
                declan = declan + int(pointsAdded)
                print(declan)
            else:
                if(name == "altair"):
                    altair = altair + int(pointsAdded)
                    print(altair)
                else:
                    if(name == "jamil"):
                        jamil = jamil + int(pointsAdded)
                        print(jamil)
                    else:
                        if(name == "matt"):
                            matth = matt + int(pointsAdded)
                            print(matt)
                        else:
                            if(name == "dallis"):
                                    dallis = dallis + int(pointsAdded)
                                    print(dallis)
                            else:
                                if(name == "lola"):
                                    lola = lola + int(pointsAdded)
                                    print(lola)
                                else:
                                    if(name == "kai"):
                                        kai = kai + int(pointsAdded)
                                        print(kai)
                                    else:
                                        if(name == "matthew"):
                                            matthew = matthew + int(pointsAdded)
                                            print(matthew)
                                        else:
                                            barb = barb + int(pointsAdded)
                                            print(barb)

addMore = input("Do you want to add")
