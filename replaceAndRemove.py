def replace_and_remove(size, s):
    #forward iteration: remove b's and count the number of a's
    write_idx, a_count = 0, 0
    for i in range(size):
        if s[i]!='b':
            s[write_idx]=s[i]
            write_idx+=1
        if s[i] == 'a':
            a_count += 1

    #backward iteration: replace 'a's with dd's starting from the end
    cur_idx = write_idx - 1
    write_idx += a_count - 1
    final_size = write_idx + 1
    while cur_idx>=0:
        if s[cur_idx] == 'a':
            s[write_idx-1:write_idx+1] = 'dd'
            write_idx =- 2
        else:
            s[write_idx] = s[cur_idx]
            write_idx -= 1
        cur_idx -= 1
    return final_size

print(replace_and_remove(7, ['a','c','d','b','b','c','a']))
print(replace_and_remove(7, ['a','b','b','b','b','b','a']))