a = int(input("Enter Number: "))
b = int(input("Enter Number: "))
c = int(input("Enter Number: "))
d = int(input("Enter Number: "))
e = int(input("Enter Number: "))
f = int(input("Enter Number: "))
g = int(input("Enter Number: "))

list = [a,b,c,d,e,f,g]
r = int(input("Enter A Number: "))
for i in range(len(list)):
    if r == list[i]:
        print(f"The Number in list is found {i+1} position")