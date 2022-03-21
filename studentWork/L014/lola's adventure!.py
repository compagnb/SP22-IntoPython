#choose lola's adventure!

intro = "barb was waiting for all the student to show up. Lola did not want to came to class today.lola would much rather have been playing ROBLOX and face timeing her friend."

goToClass = "lola had so much fun programming, she started hacking ROBLOX" 

goHome = "when lola left she was eaten by a dinosaur!"

print(intro)
choice1 = input("will lola go to class? Please type yes or no")
if(choice1 == "no"):
    print(goHome)
else:
    print(goToClass)
