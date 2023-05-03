import time

def print_pause(message):
    print(message)
    time.sleep(2)

def intro():
    print_pause("You wake up in a dark room with no memory of how you got there.")
    print_pause("You look around and see a door and a window.")

def door_room():
    print_pause("You try the door, but it's locked.")
    print_pause("You look around and see a key on a nearby table.")
    while True:
        choice = input("Do you want to take the key? (y/n)\n")
        if choice == "y":
            print_pause("You take the key and try it in the door.")
            print_pause("The door unlocks and you escape!")
            break
        elif choice == "n":
            print_pause("You leave the key and go back to exploring.")
            break
        else:
            print_pause("Sorry, I didn't understand that.")

def window_room():
    print_pause("You look out the window and see that you're on the second floor.")
    print_pause("You notice a tree close by.")
    while True:
        choice = input("Do you want to jump out the window and try to reach the tree? (y/n)\n")
        if choice == "y":
            print_pause("You jump out the window and land safely in the tree.")
            print_pause("You climb down and run away to freedom!")
            break
        elif choice == "n":
            print_pause("You decide to keep looking for another way out.")
            break
        else:
            print_pause("Sorry, I didn't understand that.")

def play_game():
    intro()
    while True:
        choice = input("Do you want to try the door or the window?\n")
        if choice == "door":
            door_room()
            break
        elif choice == "window":
            window_room()
            break
        else:
            print_pause("Sorry, I didn't understand that.")

play_game()
