def longest_subarray_with_distinct_entries(A):
    most_recent_occurrence = {}
    longest_dup_free_subarray_start_idx = result = 0

    for i, a in enumerate(A):
        #Defer updating dup_idx until we see a duplicate
        if a in most_recent_occurrence:
            dup_idx = most_recent_occurrence[a]
            #A[i] appeared before. Did it appear in the longest current subarray?
            if dup_idx >= longest_dup_free_subarray_start_idx:
                result = max(result, i - longest_dup_free_subarray_start_idx)
                longest_dup_free_subarray_start_idx = dup_idx + 1
        most_recent_occurrence[a] = i

    return max(result, len(A) - longest_dup_free_subarray_start_idx)

print(longest_subarray_with_distinct_entries(['f', 's', 'f', 'e', 't', 'w', 'e', 'n', 'w', 'e']))
print(longest_subarray_with_distinct_entries(['a','b','b','c','c','a']))