# Complete the solve function below.
def solve(s):
    
    l = s.split(" ")
    
    string = list(map(lambda s: s.capitalize() if s.isalpha() else s,l))
    
    return " ".join(string)
    
if __name__ == '__main__':
    s = input()

    result = solve(s)

    print(result)