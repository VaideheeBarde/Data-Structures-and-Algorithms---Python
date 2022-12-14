def decompose_into_dictionary_words(domain, dictionary):
    last_length = [-1] * len(domain)

    for i in range(len(domain)):
        if domain[:i+1] in dictionary:
            last_length[i] = i+1
            continue

    for j in range(i):
        if last_length[j] != -1 and domain[j + 1: i + 1] in dictionary:
            last_length[i] = i - j
            break

    decompositions = []

    if last_length[-1] != -1:
        idx = len(domain) - 1
        while idx>=0:
            decompositions.append(domain[idx + 1 - last_length[idx]:idx + 1])
            idx -= last_length[idx]

        decompositions = decompositions[::-1]

    return decompositions

print(decompose_into_dictionary_words('amanaplanacanal', {'a', 'man', 'a', 'plan', 'a', 'canal'}))