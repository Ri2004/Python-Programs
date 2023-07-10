print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_str = name1 + name2
lower_case_str = combined_str.lower()

t = lower_case_str.count('t')
r = lower_case_str.count('r')
u = lower_case_str.count('u')
e = lower_case_str.count('e')

l = lower_case_str.count('l')
o = lower_case_str.count('o')
v = lower_case_str.count('v')
e = lower_case_str.count('e')

score = str(t+r+u+e)+str(l+o+v+e)
if int(score)<10 or int(score)>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif int(score)>=40 and int(score)<=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")