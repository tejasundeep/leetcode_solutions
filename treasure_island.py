import random

direction = input("""You have a cross road where you wanna go?
1. Left
2. Right
""")
direction = int(direction)

choice_1 = [1, 2]
choice_2 = [1, 2]
choice_3 = [1, 2, 3]

if direction == random.choice(choice_1):
    print("You reached graveyard! You failed hunting the treasure!")
else:
    island = input("""You reached a beautiful island. There is a big river infront!
1. I will swim
2. I will wait for a boat
""")
    island = int(island)
    if island == choice_2:
        print("Treseasure gaurdians killed you, You lost the treasure")
    else:
        box = input("""You have three boxes infront, Which one do you choose?
1. Gold
2. Silver
3. Bronze
""")
        box = int(box)
        if box == choice_3:
            print("Hurray the treasure is yours!!!")
        else:
            print("The protecting gaurdian killed you, You lost treasure")