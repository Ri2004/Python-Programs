rows = int(input("Enter Row Size: "))
cols = int(input("Enter Column Size: "))

matrix1 = []
matrix2 = []
sum_matrix = []

for i in range(rows):
    row1 = []
    for j in range(cols):
        elements_of_1st_matrix = int(input(f"Enter 1st Matrix Elements at position [{i}][{j}]: "))
        row1.append(elements_of_1st_matrix)
    matrix1.append(row1)
    
print()

for i in range(rows):
    row2 = []
    for j in range(cols):
        elements_of_2nd_matrix = int(input(f"Enter 2nd Matrix Elements at position [{i}][{j}]: "))
        row2.append(elements_of_2nd_matrix)
    matrix2.append(row2)

print()

for i in range(rows):
    row3 = []
    for j in range(cols):
        addition = matrix1[i][j] + matrix2[i][j]
        row3.append(addition)
    sum_matrix.append(row3)
     
print("1st Matrix is:")   
for x in matrix1:
    print(x)
    
print()

print("2nd Matrix is:")  
for y in matrix2:
    print(y)
    
print()

print("Addition Of 1st and 2nd Matrix is:")  
for z in sum_matrix:
    print(z)