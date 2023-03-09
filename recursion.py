def palindrome(s):
    ''' 
    - if a string is 0 or one letter long
    - if a string has the first and last letters the same, and the remaining letters are a palindrome
    - if the slice [1: -1]
    '''
    return len(s) < 2 or s[0] == s[-1] and palindrome(s[1:-1])

print(palindrome('kayak'))