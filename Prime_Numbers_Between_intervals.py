def check_prime(n):
    prime = True
    if n==0 or n==1:
        prime = False
    else:
        for i in range(2,n):
            if n%i == 0:
                prime = False
                break
    return prime
                
a = int(input("Enter Low Limit: "))
b = int(input("Enter Upper Limit: "))
for i in range(a, b+1):
    if check_prime(i):
        print(i)