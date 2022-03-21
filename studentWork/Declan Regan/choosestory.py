#choose Lola's day

intro = "barb was waiting in Hauser Hall for all of the students to show up.Lola did not want to go to class today. Lola would much rather have been playing roblox and watching vidoes on the computer. Barb told Lola we had a fun lesson planed for today."


gotoClass = "At class they had a pizza party."
goHome = "Lola ate cheatoes in here bed playing vidoe games all day"
print(intro)
choice1 = input("Will lola go to class? Y or N")
if(choice1 == "Y"):
    print(gotoClass)    
elif(choice1 == "N"):
    print(goHome)
