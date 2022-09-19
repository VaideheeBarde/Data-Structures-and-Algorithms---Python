import collections

def is_letter_constructible_from_magazine_pythonic(letter_text, magazine_text):
    return (not collections.Counter(letter_text) - collections.Counter(magazine_text))

print(is_letter_constructible_from_magazine_pythonic('abcde', 'bedca'))
print(is_letter_constructible_from_magazine_pythonic('abcdee', 'bedca'))