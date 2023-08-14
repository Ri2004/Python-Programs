from calculator_art import logo
from replit import clear
print(logo)

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

def calculator():
    num1 = float(input("What is the first number? "))

    for symbol in calculator_operators:
        print(symbol)

    end_calculation = False
    while not end_calculation:
        operator_symbol = input("Pick a symbol from the above line: ")
        num2 = float(input("What is the next number? "))
        calculation = calculator_operators[operator_symbol]
        answer = calculation(num1, num2)

        print(f"{num1} {operator_symbol} {num2} = {answer}")

        if input(f"Type 'y' to calculating with {answer}, or type 'n' to start a new calculation.: ").lower() == 'y':
            num1 = answer
        else:
            clear()
            end_calculation = True
            calculator()

calculator()