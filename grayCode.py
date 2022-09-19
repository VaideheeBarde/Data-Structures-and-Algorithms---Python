#An n-bit Gray code is a permutation of {0, 1, 2, ...., 2^n - 1} such that the 
#binary representation of successive integers in the sequence differ in only one place
#This is with wraparound i.e. that last and first elements must also differ in only one place

def gray_code(num_bits):
    def directed_gray_code(history):
        def differs_by_one_bit(x, y):
            bit_difference = x ^ y
            return bit_difference and not (bit_difference & bit_difference - 1)

        if len(result) == 1 << num_bits:
            #Check if the first and last codes differ by one bit
            return differs_by_one_bit(result[0], result[-1])

        for i in range(num_bits):
            previous_code = result[-1]
            candidate_next_code = previous_code ^ (1 << i)
            if candidate_next_code not in history:
                history.add(candidate_next_code)
                result.append(candidate_next_code)
                if directed_gray_code(history):
                    return True
                del result[-1]
                history.remove(candidate_next_code)

        return False

    result = [0]
    directed_gray_code(set([0]))
    return result

print(gray_code(3))