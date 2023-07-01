list = []
n = int(input("Enter A Number: "))
sum = 0 
for i in range(1, n+1):
    sum += i**2
    list.append(i**2)
print(list)
print("Sum Of Natural Numbers: ", sum)