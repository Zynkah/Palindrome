from collections import deque

def palchecker(aString):
    chardeque = deque()

    # iterate the letters in the string
    for ch in aString:
        chardeque.appendleft(ch)

    stillEqual = True

    while len(chardeque) > 1 and stillEqual:
        # removes first and last letter and compares if they are equal
        first = chardeque.pop()
        last = chardeque.popleft()
        if first != last:
            # if they are different letters, return false
            stillEqual = False
        
    return stillEqual

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))