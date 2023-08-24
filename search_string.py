def checkStringInOrNot(haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    return -1


haystack = input("Enter First String: ")
needle = input("Enter Second String: ")

check = checkStringInOrNot(haystack, needle)
print(check)