Year = int(input("Enter Year: "))
if Year % 4==0:
    print(f"{Year} is a Leap Year")
elif Year % 100!=0:
    print(f"{Year} is a Leap Year")
elif Year % 400==0:
    print(f"{Year} is a Leap Year")
else:
    print("Not Leap Year")