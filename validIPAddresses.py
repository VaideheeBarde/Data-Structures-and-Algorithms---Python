def valid_ip_addresses(s):
    def is_valid_part(s):
        return len(s)==1 or (s[0] != '0' and int(s) <= 255)

    result , parts = [], ['']*4

    for i in range(1, min(4, len(s))):
        parts[0] = s[:i]
        if is_valid_part(parts[0]):
            for j in range(1, min(4, len(s)-i)):
                parts[1] = s[i:i+j]
                if is_valid_part(parts[1]):
                    for k in range(1,  min(4,len(s)-i-j)):
                        parts[2], parts[3] = s[i+j:i+j+k], s[i+j+k:]
                        if is_valid_part(parts[2]) and is_valid_part(parts[3]):
                            result.append('.'.join(parts))

    return result

print(valid_ip_addresses("19216811"))