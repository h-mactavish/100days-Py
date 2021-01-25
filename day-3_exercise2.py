# BMI Calculator v2.0

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
height = float(height)
weight = float(weight)
bmi = round(weight/(height*height))

if bmi <= 18.5:
    print(f"Your BMI is {bmi},you are underweight")
elif bmi > 18.5 and bmi <= 25:
    print(f"Your BMI is {bmi},you are normal weight")
elif bmi > 25 and bmi <= 30:
    print(f"Your BMI is {bmi},you are overweight weight")
elif bmi > 30 and bmi <= 35:
    print(f"Your BMI is {bmi},you are obese")
elif bmi > 35:
    print(
        f"Your BMI is {bmi},you are CLINICALLY OBESE.STOP EATING FOR F'S SAKE")
