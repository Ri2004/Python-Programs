import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

length = len(names)
random_num = random.randint(0, length-1)

person_will_pay = names[random_num]
print(f"{person_will_pay} is going to buy the meal today!")