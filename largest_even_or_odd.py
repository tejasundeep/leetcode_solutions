totalCount = int(input("Enter the total number of elements of the given list = "))
given_list = []

for i in range(totalCount):
    eleme = int(input("Enter some random element(integer) = "))
    given_list.append(eleme)
    
even_list = []
odd_list = []

for eleme in given_list:    
    if(eleme % 2 == 0):
        even_list.append(eleme)
        
    else:
        odd_list.append(eleme)
        
even_list.sort()
odd_list.sort()

print("The Largest even number in the given list", given_list, "=", even_list[-1])
print("The Largest odd number in the given list", given_list, "=", odd_list[-1])