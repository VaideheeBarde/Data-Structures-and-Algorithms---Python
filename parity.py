#Method 1

def parity(x):
    
    result = 0

    while x:
        result ^= x & 1
        x>>=1
    return result

print(parity(7))

#Method 2

def parity1(x):
    result = 0

    while x:
        result ^= 1
        x &= x-1

    return result

print(parity1(7))

#Method 3

def parity2(x):
    x^=x>>32
    x^=x>>16
    x^=x>>8
    x^=x>>4
    x^=x>>2
    x^=x>>1

    return x & 0x1

print(parity2(7))

#Method 4

def parity3(x):
    mask_size = 16
    bit_mask = 0xFFFF
    return (PRECOMPUTED_PARITY[x>>(3*mask_size)] ^ PRECOMPUTED_PARITY[(x>>(2*mask_size)) & bit_mask] ^ PRECOMPUTED_PARITY[(x>>mask_size) & bit_mask] ^ PRECOMPUTED_PARITY[x & bit_mask])