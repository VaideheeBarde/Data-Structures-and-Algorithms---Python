cache = {}

def fibonacci(n):
    if n <= 1:
        return n
    elif n not in cache:
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return cache[n]

print(fibonacci(3))
print(fibonacci(5))
print(fibonacci(10))

#O(n) time
#O(n) space 