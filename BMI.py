weight = int(input("Enter Weight in kg: "))
height = float(input("Enter Height in meter: "))

bmi = weight / (height * height)
print(f"The BMI is {int(bmi)}")