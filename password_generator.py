import random

password = input("How many digit password you want?: ")
password = int(password)

alphabets = "abcdefghijklmnopqrstuvwxyz"

alphabet = []
for i in alphabets:
    alphabet.append(i)

number = []
for j in range(10):
    number.append(j)

symbol = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

strong_password = alphabet + number + symbol
random.shuffle(strong_password)

list = []
for i in range(password):
    list.append(strong_password[i])

your_password = ''.join(map(str, list))
print(your_password)