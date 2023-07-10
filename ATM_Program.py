a = int(input("Enter Initial Amount: "))
choice = input("Choose\n c for credit\n d for debit\n b for balance\n")

if choice == 'c':
    print(f"Yor Balance Amount is: {a}")
    deposit = int(input("Enter Deposit Amount: "))
    
    if deposit>0:
        print(f"Your Balance Amount is {a+deposit}")
elif choice == 'd':
    print(f"Yor Balance Amount is: {a}")
    withdraw = int(input("Enter Debit Amount: "))
    
    if withdraw<a:
        print(f"Your Balance Amount is {a-withdraw}")
    elif withdraw>a:
        print("Nothing to withdraw")
        
elif choice == 'b':
    print(f"Balance Amount is {a}")
else:
    print("Invalid input")

