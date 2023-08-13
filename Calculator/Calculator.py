





from calculator_art import logo
print(logo)

end_calculation = False

def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

calculator_operators = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

num1 = int(input("What is the first number? "))

for symbol in calculator_operators:
    print(symbol)

operator_symbol = input("Pick a symbol from the above line: ")
num2 = int(input("What is the second number? "))
calculation = calculator_operators[operator_symbol]
answer = calculation(num1, num2)
first_answer = answer

print(f"{num1} {operator_symbol} {num2} = {answer}")

while not end_calculation:
    choice = input(f"Type 'y' to calculating with {answer}, or type 'n' to exit.: ").lower()
    if choice == 'y':
        operator_symbol = input("Pick another symbol: ")
        num3 = int(input("What is next number? "))
        calculation = calculator_operators[operator_symbol]
        answer = calculation(answer, num3)
        next_answer = answer
        print(f"{answer} {operator_symbol} {num3} = {next_answer}")

    else:
        end_calculation = True