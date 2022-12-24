number = int(input("Enter Number: "))

for i in range(2, number+1):
    if(number % i == 0):
        print(f'The smallest number which divides the given number is {i}')
        break