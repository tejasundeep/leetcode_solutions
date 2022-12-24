def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list
 

print("1. Check weather number is prime || 2. Get the list of prime numbers in the range")
prime_type_check = input("Enter Type: ")
prime_type_check = int(prime_type_check)

if(prime_type_check == 1):
    num = input("Enter Number: ")
    num = int(num)
    if num > 1:    
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                print(num, " is not a prime number")
                break
        else:
            print(num, " is a prime number")
    
    else:
        print(num, " is not a prime number")
else:
    starting_range = input("Starting Range: ")
    ending_range = input("Ending Range: ")

    starting_range = int(starting_range)
    ending_range = int(ending_range)

    list = prime(starting_range, ending_range)
    if len(list) == 0:
        print("There are no prime numbers in this range")
    else:
        print("The prime numbers in this range are: ", list)