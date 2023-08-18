if __name__ == '__main__':
    alist = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        alist.append([name, score])
second_highest = sorted([score1 for name, score1 in alist])[0]
print('\n'.join(sorted([name1 for name1, score in alist if score == second_highest])))