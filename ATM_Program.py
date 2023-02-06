a = int(input("Enter Initial Amount: "))
choice = input("Choose\n c for credit\n d for debit\n b for balance\n")

if choice == 'c':
    c = int(input("Enter Credit Amount: "))
    print(f"Credited Amount is {a+c}")
elif choice == 'd':
    d = int(input("Enter Debit Amount: "))
    print(f"Debited Amount is {a-d}")
elif choice == 'b':
    print(f"Balance Amount is {a}")
else:
    print("Invalid input")

