a = int(input("Enter A Number: "))
b = int(input("Enter A Number: "))
c = int(input("Enter A Number: "))

if(a<b and a<c):
    print(f"{a} is smallest")

if(b<a and b<c):
    print(f"{b} is smallest")

if(c<a and c<b):
    print(f"{c} is smallest")