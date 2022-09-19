def palindrome_decompositions(text):
    def directed_palindrome_decompositions(offset, partial_partition):
        if offset == len(text):
            result.append(partial_partition.copy())
            return

        for i in range(offset + 1, len(text) + 1):
            prefix = text[offset:i]
            if prefix == prefix[::-1]:
                directed_palindrome_decompositions(i, partial_partition + [prefix])

    result = []
    directed_palindrome_decompositions(0, [])
    return result

print(palindrome_decompositions('0204451881'))