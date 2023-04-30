a = int(input("Enter A Number: "))
b = int(input("Enter A Number: "))
c = int(input("Enter A Number: "))

alpha = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
beta = (-b - (b**2 - 4*a*c)**0.5)/(2*a)

print(f"The solution of Quadratic Equation is {alpha} and {beta}")