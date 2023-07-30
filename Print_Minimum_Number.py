student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

lowest_score = student_scores[0]
for min_num in range(1, len(student_scores)):
    if lowest_score > student_scores[min_num]:
        lowest_score = student_scores[min_num] 

print(f"The lowest score in the class is: {lowest_score}")