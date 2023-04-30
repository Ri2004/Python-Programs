num = int(input("Enter A Number: "))
temp = num
dig = 0

while num>0:
    digit = num%10
    rem = digit**3
    dig = dig+rem  
    num = num//10
    
if temp == dig:
    print(f"{temp} is an Armstrong Number")
else:
    print(f"{temp} is not an Armstrong Number")