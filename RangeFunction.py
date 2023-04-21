def wscube(*args):
    p = len(args)
    r = []
    if  p == 1:
        
        i = 0
        
        if args[0] > 0:
            while i<args[0]:
                r.append(i)
                i += 1
        
        elif args[0]<0:
            while i>args[0]:
                r.append(i)
                i = i - 1
    
    elif p == 2:
        i = args[0]
        
        if args[1] > 0:
            while i<args[1]:
                r.append(i)
                i += 1
        
        elif args[1]<0:
            while i>args[1]:
                r.append(i)
                i = i - 1
    
    elif p ==3:
        i = args[0]
        
        if args[2] > 0:
            while i<args[1]:
                r.append(i)
                i = i + args[2]
                
        elif args[2]<0:
            while i>args[1]:
                r.append(i)
                i = i + args[2]
                
        elif args[2]==0:
            print("Wrong input")
        
        else:
            print("Wrong input")
            
    else:
        print("Wrong input")
        
    return tuple(r)

for p in wscube(1,15,2):
    print(p)          
        