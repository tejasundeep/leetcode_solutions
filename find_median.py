
total_numbers = int(input("Enter total numbers: "))
list = []

for i in range(total_numbers):
    list.append(input(f"Enter number {i+1}: "))

list.sort()
list_length = len(list)
middle_value = (list_length - 1)//2
if(list_length % 2 == 0):
    result_value = (list[middle_value] + list[middle_value+1])/2
else:
    result_value = list[middle_value]

print('The median of the given list of elements: ', result_value)