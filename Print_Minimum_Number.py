student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

lowest_score = 0
for min_num in student_scores:
    if min_num > lowest_score:
        lowest_score = min_num 

print(f"The highest score in the class is: {lowest_score}")