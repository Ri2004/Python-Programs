num = int(input("Enter A Number: "))
temp = num
reverse = 0
while(num>0):
    digit = num%10
    reverse = reverse *10 + digit
    num = num//10
    
if temp == reverse:
    print(f"{temp} is a Palindrome Number")
else:
    print(f"{temp} is not a Palindrome Number")