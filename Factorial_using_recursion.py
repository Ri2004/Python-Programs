def factorial_recursive(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial_recursive(n-1)
    
a = int(input("Enter A Number: ")) 
factorial = factorial_recursive(a)
print(factorial)