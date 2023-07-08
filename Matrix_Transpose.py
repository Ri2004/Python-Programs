rows = int(input("Enter Row Size Of Matrix: "))
cols = int(input("Enter Column Size Of Matrix: "))

matrix = []
transpose_matrix = []

for i in range(rows):
    l = []
    for j in range(cols):
        elements = int(input(f"Enter Matrix Elements at position [{i}][{j}]: "))
        l.append(elements)
    matrix.append(l)

for i in range(rows):
    list =[]
    for j in range(cols):
        matrix_element = matrix[j][i]
        list.append(matrix_element)
    transpose_matrix.append(list)

print()   
print("Before Transpose The Matrix is:")
for x in matrix:
    print(x)
    
print()
print("After Transpose The Matrix is:")
for y in transpose_matrix:
    print(y)