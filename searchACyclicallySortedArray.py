def search_smallest(A):
    left, right = 0, len(A) - 1
    while left<right:
        mid = (left + right)//2
        
        if A[mid]>A[right]:
            left = mid + 1
        else:
            right = mid
            
    return left

print(search_smallest([378,478,550,631,103,203,220,234,279,368]))