# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

# print("The max scoer in class is : "+str(max(student_scores)))

max = -1

for marks in student_scores:
    if (marks > max):
        max = marks

print(f"The max score in class is : {max}")
