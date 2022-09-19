def decoding(s):
    count, result = 0, []
    for c in s:
        if c.isdigit():
            count = count*10 +int(c)
        else:
            result.append(count*c)
            count = 0

    return ''.join(result)

print(decoding("3e4f2e"))

def encoding(s):
    result, count = [], 1

    for i in range(1,len(s)+1):
        if i == len(s) or s[i]!=s[i-1]:
            result.append(str(count)+s[i-1])
            count = 1
        else:
            count+=1

    return ''.join(result)

print(encoding("eeeffffee"))