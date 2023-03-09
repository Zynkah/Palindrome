def palindrome(s):
    return len(s) < 2 or s[0] == s[-1] and palindrome(s[1:-1])

print(palindrome('kayak'))