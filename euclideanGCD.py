def gcd(x, y):
    return x if y == 0 else gcd(y, x%y)

print(gcd(30, 50))
print(gcd(5, 3))
print(gcd(18, 99))