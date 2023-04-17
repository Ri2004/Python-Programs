email = input("Enter your email address: ")

p = 0 # p is for valid email
c = 0 # c is for invalid email

if " " not in email:
    if (email.count("@") == 1) and (email.count(".") == 1):
        if len(email) > 8 :
            if email[0].isalpha():
                user,comp,domain = email[:email.index("@")], email[email.index("@")+1:email.index(".")], email[email.index(".")+1:]
                
                if len(domain)>1 and len (domain)<4:
                    if domain.islower():
                        p = p+1
                    else:
                        c = c+1
                        
                    if comp.isalpha():
                        p = p+1
                    else:
                        c = c+1
                    
                    for ch in user:
                        if ch.isalnum()  or ch == "_":
                            p = p+1
                        else:
                            c = c+1
                else:
                    c = c+1
            else:
                c = c+1
        else:
            c = c+1
    else:
        c = c+1
else:
    c = c+1
    
if c != 0 :
    print("Invalid Email")
elif c==0 or p!=0:
    print("Valid Email")