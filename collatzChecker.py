#Take any natural number
#If it is odd, triple it and add one; if it is even, halve it
#Repeat the process indefinitely, you'll eventually arrive at 1

def test_collatz_conjecture(n):
    #Stores odd numbers already tested to converge to 1
    verified_numbers = set()

    #Starts from 3, hypothesis holds trivially for 1
    for i in range(3, n+1):
        sequence = set()
        test_i = i

        while test_i >= i:
            if test_i in sequence:
                #We previously encountered test_i, so the Collatz sequence has fallen into a loop
                #This disproves the hypothesis, so we short-circuit, returning False
                return False
            sequence.add(test_i)

            if test_i % 2: #Odd number
                if test_i in verified_numbers:
                    break #test_i has already been verified to converge to 1
                verified_numbers.add(test_i)
                test_i = 3 * test_i + 1
            else:
                test_i //= 2 #Even number, halve it

    return True

print(test_collatz_conjecture(11))