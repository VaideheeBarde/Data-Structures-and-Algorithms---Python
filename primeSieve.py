def generate_primes(n):
    if n<2:
        return []
    size = (n-3)//2+1
    primes = [2]

    #stores the primes from 1 to n
    #is_prime[i] represents (2i+3) is prime or not
    #for example, is_prime[0] represents 3 is prime or not, 
    #is_prime[1] represents 5, is_prime[2] represents 7 etc.
    #Initially set each to true
    #Then use sieving to eliminate non primes

    is_prime = [True] * size
    for i in range(size):
        if is_prime[i]:
            p = i*2+3
            primes.append(p)
            #sieving from p^2, where p^2 = (4i^2 + 12i + 9)
            #note that we need to use long for j since p^2 may overflow
            for j in range(2*i**2 + 6*i + 3, size, p):
                is_prime[j] = False

    return primes

print(generate_primes(20))