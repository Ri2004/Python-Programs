num = int(input("Enter A Number: "))
temp = num
reverse = 0
while(temp>0):
    digit = temp%10
    reverse = reverse *10 + digit
    temp = temp//10
    
if num == reverse:
    print(f"{num} is a Palindrome Number")
else:
    print(f"{num} is not a Palindrome Number")