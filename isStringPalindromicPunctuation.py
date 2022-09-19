def is_palindrome(s):
    #i moves forward
    #j moves backward
    i, j = 0, len(s)-1
    while i<j:
        #i and j both skip non-alphanumeric characters
        while not s[i].isalnum() and i<j:
            i += 1
        while not s[j].isalnum() and i<j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i, j = i+1, j-1

    return True

print(is_palindrome("A man, a plan, a canal, Panama"))