#choose Lola's adventure!

intro = "Barb was waiting in Hauser Hall for all of the students to show up. Lola did not want to go to class today. Lola would rather have been playing RoBlox and watching videos on the computer. Barb told Lola we had a fun lesson for today."

goToClass = "Oh no! Lola forgot her umbrella! She came to class soaked and the computer broke because the water got into it. She should have stayed home."
goHome = "Oh no! She spilled water while she was washing her hands! She also broke the computer while hacking RoBlox because the water got into it. She should have went to class instead of staying home."
goToClass1 = "When Lola got home, she tells her mom what happens. Her mom enrolls her at a different class and she never learns Python."
goToClass2 = "Lola goes to a different computer and breaks it so she dried herself and then chose a different computer. She learned Python so she is happy."
goHome1 = "Lola's mom caught her hacking and bans computer for life. Her mom also unenrolled from Python class."
goHome2 = "Lola reads her favorite book and enjoys the rest of the day."
print(intro)
choice1 = input("Will Lola go to class? (yes/no)")
if(choice1 == "yes"):
    print(goToClass)
    choice11 = input("Will Lola go home crying? (yes/no)")
    if(choice11 == "yes"):
        print(goToClass1)
    else:
        print(goToClass2)
else:
    print(goHome)
    choice12 = input("Will Lola use her mom's computer to hack RoBlox? (yes/no)")
    if(choice12 == "yes"):
        print(goHome1)
    else:
        print(goHome2)
