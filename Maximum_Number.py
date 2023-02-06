a = int(input("Enter First Number: "))
b = int(input("Enter Second  Number: "))
c = int(input("Enter Third  Number: "))
d = int(input("Enter Fourth Number: "))
e = int(input("Enter Fifth Number: "))
f = int(input("Enter Sixth Number: "))

if a>b:
    num1 = a
else:
    num1 = b

if c>d:
    num2 = c
else:
    num2 = d

if e>f:
    num3 = e
else:
    num3 = f

if num1>num2 and num1>num3:
    print(f"{num1} is maximum")

if num2>num1 and num2>num3:
    print(f"{num2} is maximum")

if num3>num1 and num3>num2:
    print(f"{num3} is maximum")