print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_number = int(input("How many people to split the bill? "))

tip = tip/100
total_tip_amount = bill * tip
total_bill = bill + total_tip_amount
bill_per_person = total_bill/people_number
final_amount = round(bill_per_person,2)
print(f"Each person should pay: ${final_amount}")