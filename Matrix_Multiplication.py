rows1 = int(input("Enter Row Size Of 1st Matrix: "))
cols1 = int(input("Enter Column Size Of 1st Matrix: "))

rows2 = int(input("Enter Row Size Of 2nd Matrix: "))
cols2 = int(input("Enter Column Size Of 2nd Matrix: "))

matrix1 = []
matrix2 = []

if cols1 !=  rows2:
    print("Multiplication Not Possible")
else:
    for i in range(rows1):
        l1 = []
        for j in range(cols1):
            first_matrix_element = int(input(f"Enter 1st Matrix Element at position [{i}][{j}]: "))
            l1.append(first_matrix_element)
        matrix1.append(l1)
        
    print()
 
    for k in range(rows2):
        l2 = []
        for m in range(cols2):
            second_matrix_element = int(input(f"Enter 2nd Matrix Element at position [{k}][{m}]: "))
            l2.append(second_matrix_element)
        matrix2.append(l2)
    
    print()
    
    print("1st Matrix:")
    for s in matrix1:
        print(s)
        
    print()
    print("2nd MAtrix:")
    for t in matrix2:
        print(t)
    
    print()
    print("After Multiplication Resultant Matrix is:")
    for x in range(rows1):
        for y in range(cols2):
            sum = 0
            resultant_matrix = []
            for z in range(0, rows1+1 and cols2+1):
                sum = sum + (matrix1[x][z] * matrix2[z][y])
            resultant_matrix.append(sum)
            print(resultant_matrix, end="")
        print()