def is_perfect_square(n):
    s = int(n**0.5)
    return s*s == n
def check_fibonacci(num):
    return is_perfect_square(5*num**2+4) or is_perfect_square(5*num**2-4)

start = int(input("Enter Lower Limit: ")) 
end = int(input("Enter Upper Limit: "))

for i in range(start, end+1):
    if check_fibonacci(i) == True:
        print(f"{i} is a Fibonacci Number")
    else:
        print(f"{i} is not a Fibonacci Number")