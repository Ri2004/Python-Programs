def sum_recursive(n):
    if n==1:
        return 1
    else:
        return n + sum_recursive(n-1)
    
a = int(input("Enter Number: "))
sum = sum_recursive(a)
print(sum)