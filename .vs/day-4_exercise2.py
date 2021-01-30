import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

length_l = len(names)
print(length_l)
random_pick = random.randint(0, length_l-1)
# print(random_pick)
print(names[random_pick]+" is going to buy the meal today")
