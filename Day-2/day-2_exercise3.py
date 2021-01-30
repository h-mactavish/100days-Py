# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
total_days = 90*365
total_weeks = 90*52
total_months = 90*12
total_left = total_days-(int(age)*365)
total_left_weeks = total_weeks-(int(age)*52)
total_left_months = total_months-(int(age)*12)

months = total_left//12
print(
    f"You have {total_left} days, {total_left_weeks} weeks and {total_left_months} months left.")
