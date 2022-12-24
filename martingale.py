amount = input("Intital Amount: ")
martingale = input("Martingale Count: ")

amount = float(amount)
martingale = float(martingale)

result = amount*(pow(2, martingale))

print(result)