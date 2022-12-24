amount = input("Enter Amount: ")
time = input("Enter Loan Period: ")
roi = input("Enter rate of interest: ")

interest = (int(amount) * int(time) * int(roi))/100

print(interest)