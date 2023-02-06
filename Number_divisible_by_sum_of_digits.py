a = int(input("Enter A Number: "))
sum = 0
n = a
while (a!=0):
    b= a%10
    sum = sum + b
    a = a//10

if n%sum==0:
    print("Yes, The Number is divisible")
else:
    print("No, The Number is not divisible")