start = int(input("Enter Lower Limit: "))
end = int(input("Enter Upper Limit: "))

for i in range(start, end+1):
    temp = i
    length = len(str(i))
    
    dig = 0
    while i>0:
        rem = i%10
        # length = len(str(start))
        dig = dig + rem**length
        i //=10
    
    if temp == dig:
        print(f"{temp} is an Armstrong Number")
    else:
        print(f"{temp} is not an Armstrong Number")