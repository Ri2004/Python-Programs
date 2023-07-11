flag = False
def checkprime(n):
    is_prime = True
    if n==0 or n==1:
        is_prime = False
    else:
        for i in range(2, n//2+1):
            if n%i == 0:
                is_prime =  False
                break
        return is_prime
            
num = int(input("Enter A Positive Number: "))
for i in range(2, num//2+1):
    if checkprime(i):
        if checkprime(num-i):
            print(f"{num} = {i} + {num-i}")
            flag = True
    
if not flag:
    print(f"{num} can't be expressed as sum of two prime numbers")