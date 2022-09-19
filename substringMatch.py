#Rabin Karp algorithm
import functools

def rabin_karp(t, s):
    if len(s) > len(t):
        return -1

    base = 26

    #Hash codes for the substring of t and s
    t_hash = functools.reduce(lambda h,c: h * base + ord(c), t[:len(s)], 0)
    s_hash = functools.reduce(lambda h,c: h * base + ord(c), s, 0)
    power_s = base ** max(len(s) - 1, 0)

    for i in range(len(s), len(t)):
        #Checks the two substrings are actually equal or not, to protect against hash collision
        if t_hash == s_hash and t[i - len(s):i] == s:
            return i - len(s)

        #Uses rolling hash to compute the hash code
        t_hash -= ord(t[i - len(s)]) * power_s
        t_hash = t_hash * base + ord(t[i])

    #Tries to match s and t[-len(s):]
    if t_hash == s_hash and t[-len(s):] == s:
        return len(t) - len(s)
    return -1

print(rabin_karp('GACGCCA', 'CGC'))