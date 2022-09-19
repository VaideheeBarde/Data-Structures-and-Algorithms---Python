def h_index(citations):
    citations.sort()
    n = len(citations)
    for i, c in enumerate(citations):
        if c>= n-i:
            return n-i
    return 0

print(h_index([7,6,5,4,3,2,1]))