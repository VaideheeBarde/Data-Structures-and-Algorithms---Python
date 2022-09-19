import collections

def is_letter_constructible_from_magazine(letter_text, magazine_text):
    char_frequency_for_letter = collections.Counter(letter_text)

    #Checks if characters in magazibe_text can cover characters in 
    #char_frequency_for_letter

    for c in magazine_text:
        if c in char_frequency_for_letter:
            char_frequency_for_letter[c] -= 1
        if char_frequency_for_letter[c] == 0:
            del char_frequency_for_letter[c]
            if not char_frequency_for_letter:
                #All characters for letter_text are matched
                return True

    #Empty char_frequency_for_letter means every char in letter_text can be
    #covered by a character in magazine_text
    return not char_frequency_for_letter

print(is_letter_constructible_from_magazine('abcde', 'bedca'))
print(is_letter_constructible_from_magazine('abcdee', 'bedca'))