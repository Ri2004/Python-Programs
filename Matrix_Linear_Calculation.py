rows = int(input("Enter Row Size Of Matrix: "))
cols = int(input("Enter Column Size Of Matrix: "))

matrix = []

for i in range(rows):
    l = []
    for j in range(cols):
        element = int(input(f"Enter Matrix Elements at position [{i}][{j}]: "))
        l.append(element)
    
    matrix.append(l)

print()
print("Matrix: ")
for x in matrix:
    print(x)   

for i in range(rows):
    
    sum_of_row =0
    sum_of_cols = 0
    for j in range(cols):
        sum_of_row = sum_of_row + matrix[i][j]
        sum_of_cols = sum_of_cols + matrix[j][i]
        
    print(f"Addition of {i+1}th row: ",sum_of_row)
    print(f"Additiom of {i+1}th column: ",sum_of_cols)