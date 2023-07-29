import random 
print ("Game Start!")
user_win = 0
comp_win = 0

for i in range(1,4):
    print("Round",i)
    
    user = input("""1. Rock \n2. Paper \n3. Scissor: """)
    comp = random.choice(["Rock", "Paper", "Scissor"])
    print()
    print("Comp:", comp)
    print()
    
    if user == "Rock":
        
        if comp == "Rock":
            pass
        elif comp == "Paper":
            comp_win = comp_win+1
        elif comp == "Scissor":
            user_win = user_win+1
            
    elif user == "Paper":
        
        if comp == "Rock":
            user_win = user_win+1
        elif comp == "Paper":
            pass
        elif comp == "Scissor":
            comp_win = comp_win+1
            
    elif user == "Scissor":
        
        if comp == "Rock":
            comp_win = comp_win+1
        elif comp == "Paper":
            user_win = user_win+1
        elif comp == "Scissor":
            pass
            
    else:
        print("Invalid Input")
    
if user_win > comp_win:
    print("User Win")
if user_win < comp_win:
    print("Comp Win")
if user_win == comp_win:
    print("Match Tie")
    