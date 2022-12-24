name_one = input("Enter your name: ")
name_two = input("Enter your crush/love name: ")

true_love = "true love"

name = name_one + name_two

string_one_length = len(name_one)
string_two_length = len(name_two)
string_three_length = len(true_love)

list_true_love = []
for i in true_love:
    list_true_love.append(i)

love_score = 0
for i in range(len(list_true_love)):
    love_score = love_score + name.count(list_true_love[i])

print(f"Your love score is {(love_score/25)*100}%")