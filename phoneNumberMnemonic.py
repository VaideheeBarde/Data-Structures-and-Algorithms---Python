#input phone number - specified as a string of digits
#returns all possible character sequences that correspond to phone number
#in a phone keypad corressponds to one of three or four letters of the alphabet

#This mapping from digits to corressponding characters
MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')

def phone_mnemonic(phone_number):
    def phone_mnemonic_helper(digit):
        if digit == len(phone_number):
            #All digits are preocessed, so add partial pnemonics to pnemonics
            #(We add a copy since subsequent calls modify partial pnemonic)
            mnemonics.append(''.join(partial_mnemonic))
        else:
            #Try all possible characters fro this digit
            for c in MAPPING[int(phone_number[digit])]:
                partial_mnemonic[digit] = c
                phone_mnemonic_helper(digit + 1)

    mnemonics = []
    partial_mnemonic = [0] * len(phone_number)
    phone_mnemonic_helper(0)
    return mnemonics

print(phone_mnemonic('22'))