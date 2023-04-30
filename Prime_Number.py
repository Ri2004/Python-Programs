n = int(input("Enter A Number: "))
prime = True

if n>0:
    for i in range(2,n):  
        if n%i==0:
            prime = False
            break
    if prime:
        print(f"{n} is prime number")
    else:
        print(f"{n} is not prime number")
        
else:
    print("wrong input")