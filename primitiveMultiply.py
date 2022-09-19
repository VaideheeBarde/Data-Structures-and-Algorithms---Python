def primitive_multiply(x,y):
    def add(a,b):
        while b:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a

    running_sum = 0

    while x:
        if x & 1:
            running_sum = add(running_sum, y)
        x, y = x>>1, y<<1

    return running_sum

print(primitive_multiply(13,9))