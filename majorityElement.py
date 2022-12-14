def majority_search(stream):
    candidate_count = 0
    for it in stream:
        if candidate_count == 0:
            candidate, candidate_count = it, candidate_count + 1
        elif candidate == it:
            candidate_count += 1
        else:
            candidate_count -= 1

    return candidate

print(majority_search(['b','a','c','a','a','b','a','a','c','a']))

#O(1) time per entry
#O(n) time complexity