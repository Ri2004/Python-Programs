n = int(input("Enter A Number: "))
temp = n
sum = 0
square = n**2
while square>0:
    digit =  square%10
    sum = sum + digit
    square = square//10
    
if temp==sum:
    print(f"{n} is Neon Number")
else:
    print(f"{n} is not Neon Number")
    