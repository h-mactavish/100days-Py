# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


name1 = name1.lower()
name2 = name2.lower()

count_T = name1.count("t")+name2.count("t")
count_R = name1.count("r")+name2.count("r")
count_U = name1.count("u")+name2.count("u")
count_E = name1.count("e")+name2.count("e")

countTrue = count_T+count_R+count_U+count_E

count_L = name1.count("l")+name2.count("l")
count_O = name1.count("o")+name2.count("o")
count_V = name1.count("v")+name2.count("v")
count_E = name1.count("e")+name2.count("e")

countLove = count_L+count_O+count_V+count_E

if(countTrue*10+countLove < 10 and countTrue*10+countLove > 90):
    print(
        f"Your score is {countTrue}{countLove}, you go together like coke and mentos.")
elif(countTrue*10+countLove >= 40 and countTrue*10+countLove <= 50):
    print(f"Your score is {countTrue}{countLove}, you are alright together.")
else:
    print(f"Your score is: {countTrue}{countLove}")
