#choose Lola's adventure

intro = "Barb was waiting in Hauser Hall for all the students to show up. Lola did not want to get to class today. Lola would much rather have been playing Roblox and watching videos on the computer. Barb told Lola we had a fun lesson for today"


goToClass = "Lola had a fun time and they served pizza"
goHome = "She played tons of video games, but her dad got mad."

print (intro)
choice1 = input ("Will Lola go to class? Please type yes or no.")
if(choice1 == "yes"):
    print(goToClass)
if(choice1 == "no"):
    print(goHome)

