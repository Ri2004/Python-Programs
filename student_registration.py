print()
print("Technique Polytechnic Institute")

college = {}

fee = 0
print()
while True:
    print("Student Registration Form")
    print()
    
    student = input("""1. New Student Registration 2. Fee Submission 3. Principal Code 4. Exit\n""")
    
    print()
    
    if student == "1":
        print("New Student Registration")

        student_name = input("Enter Student Name: ")
        father_name = input("Enter Father Name: ")
        mother_name = input("Enter Mother Name: ")
        address = input("Enter Address: ")
        aadhar_number = input("Enter Aadhar Number: ")
        phone_number = int(input("Enter Mobile Number: "))
        
        print()
        
        if aadhar_number in college:
            print("Student is already registered")
        else:
            college[aadhar_number] = [student_name, father_name, mother_name, address, phone_number,fee]
            print("\nStudent is successfully registered\n")
        
        print()
        print(college)
        
    elif student == "2":
        print("Fee Submission")
        
        aadhar_number = input("Enter Aadhar Number: ")
              
        if aadhar_number in college:
            fee = int(input("Enter Fee: "))
            print()
            print("Fee is successfully submitted")
            college[aadhar_number][-1] = fee
            
            print(college)
            
        else : print("Not in College")
    
    elif student == "3":
        print("Principal Access")
        principal_code = "colltpi123"
        principal_code = input("Enter Principal Code: ")
        
        if principal_code == "colltpi123":
            aadhar_number = input("Enter Aadhar Number: ")
            
            if aadhar_number in college:
               print("Name  =" ,student_name) 
               print("Father_Name =" ,father_name)
               print("Fee =", fee)
            
            else:
                print("Not in College")
        
        else:
            print("Invalid Code")
            
    elif student == "4": 
        break
    
print("Thank You")