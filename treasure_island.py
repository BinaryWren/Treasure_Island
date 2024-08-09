print("welcome to the treasure island")
print("your mission is to find the treasure island:")
choice1 = input('you\'re at a crossroad where you can want to go "left" or "right"').lower()
if choice1 == "left":
    choice2 = input("you are come in the middle of the lake type 'wait' to wait or type 'swim' to swim in the lake").lower()
    if choice2 == "wait":
        choice3 = input("which colour do you want to choose: red, yellow, or blue?").lower()
        if choice3 == "red":
            print("game over:")
        elif choice3 == "blue":
            print("eaten by beasts game over:")
        elif choice3 == "yellow":
            print("you found a treasure: you win")
    else:
        print("you are attacked by an angry trout: game over:")
else:
    print("game is over you go to hell")