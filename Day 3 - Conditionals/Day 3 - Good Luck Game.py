print("Welcome to the game of luck (or bad luck) created by Joy (or sadness, in the case of this game)\n")
print("Here, your choice can save your life (or not)\n")
side = input("Which side do you want to go, left or right?")

if side == "right":
    print("\nYou chose the side of acoustics, and now you will relive in your mind the most distressing moment of your life. Game Over!")
    exit()
elif side == "left":
    print("\nYou have chosen the path of tranquility, and now you have the power to choose when to remain calm and collected in any situation.")
else:
    input("\nEnter a valid answer")

steps = input("\nNow you have the option to keep walking or wait until something happens, what is your choice walk or wait?")

if steps == "walk":
    print("\nYou walk and fall into an invisible floor that is an abyss that represents your existential void, so you are doomed to fall infinitely. Game Over!")
    exit()
elif steps == "wait":
    print("\nYou waited so long that you became a monk and 3 doors appeared in front of you")
else:
    input("\nEnter a valid answer")

door = input("\nWhich door do you choose: red, blue or yellow?")

if door == "red":
    print("\nRed is the color of love, you are doomed to never be able to love anyone again. Game Over!")
elif door == "yellow":
    print("\nYellow is the color of joy, and my name is joy, I'm amazing so there's no way this door can be bad. YOU WON THE GAME!")
elif door == "blue":
    print("\nBlue is the color of the sky, you are destined to always be in the clouds, that is, without paying attention to anything, that's why you were always distracted looking at the doors. Game Over!")
else:
    input("\nEnter a valid answer")

