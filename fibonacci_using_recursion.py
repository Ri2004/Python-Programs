def fibonacci_recur(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacci_recur(n-1) + fibonacci_recur(n-2)
    
num = int(input("Enter A Number: "))
print(f"Fibonacci Of ({num}) is {fibonacci_recur(num)}")