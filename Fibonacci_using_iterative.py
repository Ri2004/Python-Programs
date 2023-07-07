def fibonacci_iter(n):
    previous_num = 0
    current_num = 1
    if n==0 or n==1:
        return n
    else:
        for i in range(n-1): # We also use instead of this for i in range(1,n):
            
            pre_previous_num = previous_num
            previous_num = current_num
            current_num = pre_previous_num + previous_num
        return current_num
num1 = int(input("Enter A Number: "))
print(f"Fibonacci Of ({num1}) using iterative approach is {fibonacci_iter(num1)}")