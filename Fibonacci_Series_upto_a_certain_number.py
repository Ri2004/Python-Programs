def fibonacci(n):
    previous_num = 0 
    current_num = 1
    next_num = previous_num + current_num
    print(previous_num, current_num, end=" ")
    
    while current_num<n:
        print(next_num, end=" ")
        previous_num = current_num
        current_num = next_num
        next_num = previous_num + current_num

num = int(input("Enter A Number: "))
fibonacci(num)
    