available_exits = ["north", "south", "east", "west"]

chose_exit = ""
while chose_exit not in available_exits:
    chose_exit = input("Please choose a direction: ")
    if chose_exit.casefold() == "quit":
        print("Game over")
        break

else:
    print("aren't you glad you got out of there")