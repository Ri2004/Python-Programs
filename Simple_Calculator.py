a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print("Choose Any Operator: \n + for add \n - for subtract \n * for multiply \n / for division \n")
choice = input()
if choice == '+':
    print(f"Sum of {a} and {b} is {a+b}")
elif choice == '-':
    print(f"Subtraction of {a} and {b} is {a-b}")
elif choice == '*':
    print(f"Multiply of {a} and {b} is {a*b}")
elif choice == '/':
    print(f"Division of {a} and {b} is {a/b}")

else:
    print("Invalid input")