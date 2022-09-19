def fibonacci(n):
    if n <= 1:
        return n

    f_minus_2, f_minus_1 = 0, 1
    for _ in range(1, n):
        f = f_minus_2 + f_minus_1
        f_minus_2, f_minus_1 = f_minus_1, f
    
    return f_minus_1

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))