a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print(f"Before Swapping a = {a} and b = {b}")

a = a+b
b = a-b
a = a-b
print(f"After Swapping a = {a} and b = {b}")