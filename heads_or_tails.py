import random

choice = [1, 2]

ask = input("""
Heads or Tails?
1. Head
2. Tails
""")

if ask == random.choice(choice):
    print("You Win")
else:
    print("You Loose")