list = []
n = int(input("Enter A Number: "))
sum = 0 
for i in range(1, n+1):
    sum += i**3
    list.append(i**3)
print(list)
print("Sum Of Natural Numbers: ", sum)