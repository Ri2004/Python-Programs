rows = int(input("Enter Row Size: "))
cols = int(input("Enter Column Size: "))

matrix = []

for i in range(rows):
    list = []
    for j in range(cols):
        elements = int(input(f"Enter Matrix Elements at position [{i}][{j}]: "))
        list.append(elements)
    matrix.append(list)
    
print("Matrix:")
for i in matrix:
    print(i)