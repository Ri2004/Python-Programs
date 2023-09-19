# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

def word_count_appearence(l):
    word = OrderedDict()
    
    for words in l:
        if words not in word:
            word[words] = 1
        else:
            word[words] += 1
        
    return word
    
x = int(input())
s = set()
l = []
for _ in range(x):
    num2 = input()
    s.add(num2)
    l.append(num2)

print(len(s))

dictionary = word_count_appearence(l)

for word in dictionary:
    print(dictionary[word],end=" ")


