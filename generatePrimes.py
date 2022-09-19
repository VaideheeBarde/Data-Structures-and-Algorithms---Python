def generate_primes(n):
    primes = []
    #is_prime[p] reperesents p is prime or not
    #initially set each to true, expecting 0 and 1
    #then use sieving to eliminate non primes

    is_prime = [False, False] + [True]*(n-1)

    for p in range(2, n+1):
        if is_prime[p]:
            primes.append(p)
            #sieve p's multiples
            for i in range(p*2, n+1, p):
                is_prime[i] = False
            
    return primes

print(generate_primes(10))