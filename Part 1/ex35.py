from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("Greed leads to misfortune...")

def bear_room():
    print("There's a bear on here.")
    print("The bear has lots of honey.")
    print("The bear is in front of another door.")
    print("How will you move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear mauls you.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can now access the hidden room.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear eats you!")
        elif choice == "open door" and bear_moved:
            print("You opened the bear after the bear just moved")
            gold_room()
        else:
            print("Try \'take honey\', \'taunt bear\' or \'open door\'.")

def cthulhu_room():
    print("Here you meet the great evil Cthulhu.")
    print("It stares into you. You're slowly turning insane.")
    print("Do you stay or flee?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "stay" in choice:
        dead("You've turned insane...")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good Job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you enter?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You must pick a room!")

start()
