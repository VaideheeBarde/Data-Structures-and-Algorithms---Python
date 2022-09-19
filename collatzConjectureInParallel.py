import concurrent
from concurrent import futures

#Performs basic unit of work
def worker(lower, upper):
    for i in range(lower, upper + 1):
        assert collatz_check(i, set())
    print('(%d, %d)'%(lower, upper))

#Checks an individual number
def collatz_check(x, visited):
    if x == 1:
        return True
    elif x in visited:
        return False
    visited.add(x)
    if x & 1: #Odd Number
        return collatz_check(3 * x + 1, visited)
    #Divide by 2 for even number
    return collatz_check(x >> 1, visited)

    #Uses the library process pool for task assignment and load balancing
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        for i in range(n // range_size):
            executor.submit(worker, i * range_size + 1, (i + 1) * range_size)

num_threads = 3
worker(1, 4)