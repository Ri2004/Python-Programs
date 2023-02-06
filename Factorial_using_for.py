a = int(input("Enter a number: "))

factorial = 1
for i in range(1, a+1):
    factorial *= i
    
print(f"Factorial of {a} is: {factorial}")
    