import math
def is_perfect_square(n):
    s = int(math.sqrt(n))
    return s*s == n

def check_fibonacci(num):
    return is_perfect_square(5*num**2+4) or is_perfect_square(5*num**2-4)

number = int(input("Enter A Number: "))
if check_fibonacci(number) == True:
    print(f"{number} is a Fibonacci Number")
else:
    print(f"{number} is Not a Fibonacci Number")