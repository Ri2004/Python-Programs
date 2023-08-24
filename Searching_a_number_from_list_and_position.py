def checkNum(lis, target):
    for i in range(len(lis)):
        if lis[i] == target:
            return i
    
    return -1

num = input().split()
num = list(map(int, num))
target = int(input("Enter Target Value: "))
result = checkNum(num, target)
print(result)