# Welcome to Tip Calculator
print("Welcome to Tip Calculator.")

total_bill = float(input("What was the total bill?"))
tip = int(input("What percentage of tip would you like to give?"))
people = int(input("How many people to split the bill?"))

amount = round(((total_bill+(total_bill*(tip/100)))/people), 2)
print(f"Each person should pay {amount}")
