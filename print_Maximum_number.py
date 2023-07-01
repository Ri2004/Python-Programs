a,b,c,d,e = int(input("Enter Number: ")),int(input("Enter Number: ")),int(input("Enter Number: ")),int(input("Enter Number: ")),int(input("Enter Number: "))
list = [a,b,c,d,e]
max = list[0]
for i in range(1,len(list)):
    if max < list[i]:
        max = list[i]
        
print(f"Maximum Value From the list is: {max}")