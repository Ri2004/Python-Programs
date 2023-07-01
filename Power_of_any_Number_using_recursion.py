def power_recursive(base, power):
    if power == 0:
        return 1
    else:
        return base * power_recursive(base, power-1)
    
base = int(input("Enter Base Number: "))
power = int(input("Enter Power Number: "))
result = power_recursive(base, power)
print(result)