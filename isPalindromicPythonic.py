def isPalindromePythonic(s):
    return all(a==b for a,b in zip(map(str.lower, filter(str.isalnum, s)), map(str.lower, filter(str.isalnum, reversed(s)))))

print(isPalindromePythonic("A man, a plan, a canal, Panama"))
print(isPalindromePythonic("hello, how are you?"))