height = input("Whats your height in feet?: ")
weight = input("Whats your weight in kg?: ")

height = float(height)
weight = float(weight)

height = 0.3*height
bmi = weight/pow(height, 2)
print(f"Your BMI is: {round(bmi)}")