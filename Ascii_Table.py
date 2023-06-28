a = int(input("Enter Ascii Value: "))
b = int(input("Enter Ascii Value: "))
for ch in range(a, b+1):
    print(chr(ch), "=",ch)