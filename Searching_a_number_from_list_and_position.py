def checkNum(lis, target):
    for i in range(len(lis)):
        if lis[i] == target:
            return i
        
        elif lis[i] != target:
            lis.insert(i, target)
            lis.sort()
            return lis.index(target)

num = input().split()
num = list(map(int, num))
sorted_num = sorted(num)
print(sorted_num)
target = int(input("Enter Target Value: "))
result = checkNum(sorted_num, target)
print(result)