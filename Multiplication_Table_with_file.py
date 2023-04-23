a = int(input("Enter Number: "))
n = int(input("Enter Number: "))

for i in range(a, n+1):
    with open(f"tables/Multiplication_Table_of_{i}.txt", "w") as f:
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i*j}")
            
            if j != 10:
                f.write("\n")