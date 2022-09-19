#Runs only in python 3

import math

def square_root(x):
    #Decides the search range according to x's value relative to 1.0
    left, right = (x, 1.0) if x < 1.0 else (1.0, x)

    #Keep searching as long as left!=right
    while not math.isclose(left, right):
        mid = 0.5 * (left + right)
        mid_squared = mid * mid
        if mid_squared > x:
            right = mid
        else:
            left = mid

    return left

print(square_root(4))
print(square_root(5))