print("Wscube Car Rental System")
user_choice = 0
class car_rental_system:
    def __init__(self,cars):
        self.cars = cars
        self.database = {}
    def available_cars(self):
        print(f"Total number of cars available are {self.cars}")
        
cars = int(input("Enter the number of cars available: "))
c = car_rental_system(cars)
c.available_cars()


while True:
    choice = input("""
                   1. Rent
                   2. Deposit
                   3. Exit
                   """)
    

    if choice == "1":
        print("Rent\n 1 car for 1 day = Rs.500/-")
        ch = input("Are you sure you want to rent a car? (y/n): ")
        if ch == 'y':
            user_choice = int(input("Enter How many cars you want to rent: "))
            if user_choice <= c.cars:
                No_of_car = user_choice
                No_of_day = int(input("Enter the number of days you want to rent a car: "))
                Name = input("Enter your name: ")
                Address = input("Enter your address: ")
                Phone = int(input("Enter your phone number: "))
                Aadhar = int(input("Enter your Aadhar number: "))
                Bill = No_of_car * No_of_day * 500
                    
                agree = input("(y/n): ")
                if agree == 'y':
                    print("Successfully car booked")
                    c.database[Aadhar] = [Name,Address,Phone,Aadhar,No_of_car,No_of_day,Bill]
                    c.cars = c.cars - No_of_car
                    print("Now Available cars are: ",c.cars)
                    
                    with open("Bill_Generator.txt","a") as f:
                        f.write(Name)
                        f.write('\n')
                        f.write(Address)
                        f.write('\n')
                        f.write(str(Phone))
                        f.write('\n')
                        f.write(str(Aadhar))
                        f.write('\n')
                        f.write( str(No_of_car))
                        f.write('\n')
                        f.write(str(No_of_day))
                        f.write('\n')
                        f.write(str(Bill))
                        f.write('\n')
                        f.write("Thank you for visiting us")
                        f.write('\n\n\n\n')
                         
                elif agree == 'n':
                    print("Thank you for visiting us")
            else:
                print("Sorry, we have only",c.cars,"cars available")
                
        elif ch == 'n':
            print("Thank you for visiting us")
            
                
    
    elif choice == "2":
        print("Deposit")
        
        Aadhaar_Number = int(input("Enter your Aadhaar number: "))
        if Aadhaar_Number == c.database[Aadhaar_Number][3]:
            name = input("Enter your name: ")
            deposit = int(input("Enter the number of cars you want to deposit: "))
            if deposit > No_of_car:
                print("Not Possible")
            else:
                print("Successfully deposited")
                c.cars = c.cars + deposit
                print("now available cars are: ",c.cars)
        else:
            print("You have not rented any car")
    
    elif choice == "3":
        break
    
    else :
        print("Wrong choice")     