string = input("Enter A String: ").lower()
new_str = ""

for ch in string:
    new_str = ch + new_str

if string == new_str:
    print(string,"is a Palindrome String.")
else:
    print(string,"is not a Palindrome String.")