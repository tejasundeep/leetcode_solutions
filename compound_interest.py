principle = input("Enter Amount: ")
time = input("Enter Loan Period: ")
roi = input("Enter rate of interest: ")

amount = int(principle) * (pow((1 + int(roi) / 100), float(time)))
interest = amount - int(principle)

print(interest)