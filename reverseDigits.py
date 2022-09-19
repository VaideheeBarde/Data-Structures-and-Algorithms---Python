def reverse_bits(x):
    x_rem = abs(x)
    result = 0

    while x_rem:
        result = (result * 10) + (x_rem % 10)
        x_rem //= 10

    return -result if x<0 else result

print(reverse_bits(1132))
print(reverse_bits(-1132))