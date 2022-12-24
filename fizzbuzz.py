count = input("How man numbers you want to play?: ")
count = int(count)

for i in range(count):
    if(i % 3 == 0):
        print("Fizz")
    elif (i % 5) == 0:
        print("Buzz")
    else:
        print(i)