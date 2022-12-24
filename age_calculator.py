from datetime import datetime as dt

birth_year = input("Whats your birth year?: ")
birth_year = int(birth_year)

death = 60

current_year = int(dt.now().year)

print(f"You are {current_year - birth_year} years old, you have only {death - (current_year - birth_year)} years left to do something in life")