def fibo_series(n):
    previous_num = 0
    current_num = 1
    print(previous_num, current_num, end=" ")
    next_num = previous_num + current_num
    
    while next_num<=n:
        print(next_num, end=" ")
        previous_num = current_num
        current_num = next_num
        next_num = previous_num + current_num

num = int(input("Enter A Number: "))
fibo_series(num)