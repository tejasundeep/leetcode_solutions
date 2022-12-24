number = input("Enter Number: ")
n = int(number)

list = []
for i in range(n): 
    list.append(n-i)
list.remove(n)

result = 1
for i in range(n-1):
    result = result * list[i]

factorial = n*result
print(factorial)