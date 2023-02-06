a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))
d = int(input("Enter Fourth Number: "))
e = int(input("Enter Fifth Number: "))
f = int(input("Enter Sixth Number: "))

n = [a, b, c, d, e, f]

print("\nOdd Numbers Are")
for i in n:
    if i%2==0:
        continue
    print(i)

print("\nEven Numbers Are")
for j in n:
    if j%2==0:
        continue
    print(j)