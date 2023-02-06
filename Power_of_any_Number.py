a = int(input("Enter Base: "))
b = int(input("Enter Power: "))

result = 1
for i in range(1, b+1):
    result = result * a

print(result)