'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Example





: Append  to the list, .
: Append  to the list, .
: Insert  at index , .
: Print the array.
Output:
[1, 3, 2]
'''

if __name__ == '__main__':
    N = int(input())
List = []
for i in range(N):
    s = input().split()
    
    if s[0] == "insert":
        List.insert(int(s[1]), int(s[2]))
        
    elif s[0] == "append":
        List.append(int(s[1]))
        
    elif s[0] == "remove":
        List.remove(int(s[1]))
        
    elif s[0] == "sort":
        List.sort()
        
    elif s[0] == "print":
        print(List)
        
    elif s[0] == "pop":
        List.pop()
        
    else:
        List.reverse()