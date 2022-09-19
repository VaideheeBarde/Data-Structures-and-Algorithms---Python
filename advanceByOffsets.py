def can_reach_end(A):
    furthest_reach_so_far = 0
    last_index = len(A)-1

    i = 0
    while i<=furthest_reach_so_far and furthest_reach_so_far<last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, A[i]+i)
        i+=1

    return furthest_reach_so_far>=last_index

print(can_reach_end([3,3,1,0,2,0,1]))
print(can_reach_end([3,2,0,0,2,0,1]))