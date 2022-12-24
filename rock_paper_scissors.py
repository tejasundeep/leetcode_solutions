import random

rock = 0
scissors = 2
paper = 5

my_choice = input("Whats your choice?: ")
my_choice = int(my_choice)
choice = [0, 5, 2]

if my_choice == random.choice(choice):
    print("You Win")
else:
    print("You Loose")