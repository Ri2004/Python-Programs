n = 6
for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("* " * (n+i-6), end=" ")
    print(" " * (n-i))
    