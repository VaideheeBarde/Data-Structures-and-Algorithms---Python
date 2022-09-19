#Assume s is a list of strings, each of which is of length 1, e.g.,
#['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y']

def reverse_words(s):
    def reverse_range(s, start, finish):
        while start < finish:
            s[start], s[finish] = s[finish], s[start]
            start, finish = start + 1, finish - 1
            
    reverse_range(s, 0, len(s)-1)

    start = 0
    while True:
        finish = start
        while finish<len(s) and s[finish]!=' ':
            finish+=1
        if finish == len(s):
            break
        #reverses each word in the string
        reverse_range(s, start, finish-1)
        start = finish + 1
    
    #reverses the last word
    reverse_range(s, start, len(s)-1)

    return s
print(reverse_words(['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y']))
print(reverse_words(['I', ' ', 'a', 'm', ' ', 'a', ' ', 'd', 'e', 'v', 'e', 'l', 'o', 'p', 'e', 'r']))