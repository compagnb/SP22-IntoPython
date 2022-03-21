#choose Lola's adventure!

intro = "Barb was waiting in Hauser Hall for all of the students to show up. Lola did not want to go to class today. Lola would much rather have been playing Roblox and watching videos on the computer. Barb told Lola we had a fun lesson for today."

goToClass = "Lola had so much fun programming, she started hacking Roblox and took over the world!"

playRoblox = "Lola couldn't hack the Roblox so she lost the game and cried"
doNothing = "Lola was too bored and died"
print(intro)

choice1 = input("Will Lola go to class? Please type yes or no.")

if(choice1 == "yes"):
    print(goToClass)

else:
    choice2 = input("Is Lola going to play Roblox? Please type yes or no.")

if(choice2 == "yes"):
    print(playRoblox)

else:
    print(doNothing)
    
