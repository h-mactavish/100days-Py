# Day 3-Control Flow and Logical Operators

print("Welcome to the roller coaster ride\n")

height = int(input("Please Enter your height in cm?"))

if height >= 120:
    print("\nYou can ride the rollercoaster")
    age = int(input("Please enter your age"))
    if age < 12:
        print("Please pay $5")
    elif age >= 12 and age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("\nSorry you need to grow taller before you can ride")
