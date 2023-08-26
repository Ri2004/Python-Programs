#######################The Main Logic is#######################

# here I convert the roman numbers to its equivalent integer number. At first I reversed the roman number entered by user and store some roman value in a dictionary. After reversed the roman number I store the last roman integer in a variable and do iteration through loop and check if the value of second last roman value is less than the last roman value then subtract the value of second last roman value from the total number or result else if the value of second last roman value is greater than the last roman value then add the value of second last roman value to the total number or result

def convertToInt(s):
    roman_number = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    
    total = 0
    last_value = 0
    for result in reversed(s):
        value = roman_number[result]
        
        if value < last_value:
            total -= value
        
        else:
            total += value
        last_value = value
        
    return total
s = input("Enter Roman Number: ")
print(f"The Integer Number is: {convertToInt(s)}")
