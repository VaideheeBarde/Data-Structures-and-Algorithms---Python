import functools

def string_hash(s, modulus):
    mult = 997
    return functools.reduce(lambda v, c: (v * mult + ord(c)) % modulus, s, 0)

print(string_hash('hello', 10))