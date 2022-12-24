number = input("Enter decimal number: ")
precession = input("Enter precision: ")
number = float(number)
precession = int(precession)

result = f'%.{precession}f' % number
print("The given number upto 4 decimal places", result)