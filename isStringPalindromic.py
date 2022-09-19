def isPalindromic(s):
    #Note that s[~i] for i in [0, len(s)-1] is s[-(i+1)]
    return all(s[i] == s[~i] for i in range(len(s)//2))

print(isPalindromic("fdedf"))