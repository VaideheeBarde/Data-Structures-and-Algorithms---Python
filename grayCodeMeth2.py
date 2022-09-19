def gray_code(num_bits):
    if num_bits == 0:
        return [0]

    gray_code_num_bits_minus_1 = gray_code(num_bits - 1)

    leading_bit_one = 1 << (num_bits - 1)
    return gray_code_num_bits_minus_1 + [leading_bit_one | i for i in reversed(gray_code_num_bits_minus_1)]

print(gray_code(3))