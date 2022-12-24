query = int(input("How many number you want to calculate: "))
number = []

for i in range(query):
    number.append(input("Enter Number "+ str(i) + ": "))

total = 0
for i in range(len(number)):
    total = total + int(number[i])

print(total)