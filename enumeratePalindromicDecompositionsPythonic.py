def palindrome_decompositions_pythonic(text):
    return ([[text[:i]] + right for i in range(1, len(text) + 1) if text[:i] == text[:i][::-1] for right in palindrome_decompositions_pythonic(text[i:])] or [[]])

print(palindrome_decompositions_pythonic('0204451881'))