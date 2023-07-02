a,b,c,d,e = int(input("Enter Number: ")),int(input("Enter Number: ")),int(input("Enter Number: ")),int(input("Enter Number: ")),int(input("Enter Number: "))
list = [a,b,c,d,e]
min = list[0]
for i in range(1,len(list)):
    if min > list[i]:
        min = list[i]
        
print(f"Maximum Value From the list is: {min}")