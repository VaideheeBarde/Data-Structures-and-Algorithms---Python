def closest_int_same_bit_count(x):
    num_unsigned_bit = 64
    for i in range(num_unsigned_bit-1):
        if (x>>i) & 1 != (x>>(i+1)) & 1:
            bitmask = (1<<i) | (1<<(i+1))
            x ^= bitmask
            return x

    raise ValueError("All bits are 0 or 1")

print(closest_int_same_bit_count(10))