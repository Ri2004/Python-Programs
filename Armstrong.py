num = int(input("Enter A Number: "))
num_length = len(str(num))
temp = num
dig = 0

while num>0:
    digit = num%10
    rem = digit**num_length
    dig = dig+rem  # 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748,
    num = num//10
    
if temp == dig:
    print(f"{temp} is an Armstrong Number")
else:
    print(f"{temp} is not an Armstrong Number")