num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

choice = input("""
               +  for Addition
               - for Subtraction
               * for multiplication
               / for Division
               % for Modulus
               """)

match choice:
    case '+':
        print(f"Addition Of {num1} and {num2} is {num1 + num2}")
    case '-':
        print(f"Subtraction Of {num1} and {num2} is {num1 - num2}")
    case '*':
        print(f"Multiplication Of {num1} and {num2} is {num1 * num2}")
    case '/':
        print(f"Division Of {num1} and {num2} is {num1 / num2}")
    case '%':
        print(f"Modulus Of {num1} and {num2} is {num1 % num2}")
    case _:
        print("Invalid Input!")
