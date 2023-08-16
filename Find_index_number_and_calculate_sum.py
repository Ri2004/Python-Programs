def findindex(list, target):
    for i in range(len(list)):
        if list[i] + list[i+1] == target:
            return list.index(list[i]), list.index(list[i+1])


num = input("Enter Numbers: ").split()
convert_to_int = list(map(int, num))
target = int(input("Enter Target: "))
result = [findindex(convert_to_int, target)]
print(result)