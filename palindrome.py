def palindrome(word):
    # a word spelled the same way forward and backward
    word = word.lower()
    # returns a slice of an entire iterable in reverse
    return word[::-1] == word

print(palindrome('Mother'))
print(palindrome('Mom'))
