def swapBits(x, i, j):
    if (x>>i) & 1 != (x>>j) & 1:
        bitmask = (1<<i) | (1<<j)
        x^=bitmask
    return x

print(swapBits(2312, 0, 3))