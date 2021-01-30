# LEAP YEAR PROGRAM

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


flag = False
if year % 4 == 0:
    flag = True
    if year % 100 == 0:
        flag = False
        if year % 400 == 0:
            flag = True

if flag:
    print("This is a leap year")
else:
    print("This is not a leap year")
