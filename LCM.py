a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
lcm = 0
for i in range(1, a+1 and b+1):
    quote1 = a//i
    quote2 = b//i
    if a%i == 0 and b%i == 0:
        lcm = i*quote1*quote2
    
print(f"LCM of {a} and {b} is: {lcm}")