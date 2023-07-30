# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

sum_of_height = 0
for i in student_heights:
    sum_of_height = sum_of_height + i

total_number_of_students = 0
for number_of_students in student_heights:
    total_number_of_students += 1

avg = round(sum_of_height/total_number_of_students)

print(avg)