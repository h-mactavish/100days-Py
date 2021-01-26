# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if(size == "S"):
    size_p = 15
elif(size == "M"):
    size_p = 20
elif(size == "L"):
    size_p = 25
else:
    size_p = 0

if(add_pepperoni == "Y" and size == "S"):
    add_p = 2
else:
    add_p = 3

if(extra_cheese == "Y"):
    extra_c = 1
else:
    extra_c = 0

bill = size_p + add_p + extra_c
print(f"Your final bill is: ${bill}")
