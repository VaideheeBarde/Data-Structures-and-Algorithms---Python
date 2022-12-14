import math

class Number:
    def __init__(self, a, b):
        self.a, self.b = a, b
        self.val = a + b * math.sqrt(2)

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val

def generate_first_k_a_b_sqrt2(k):
    #Will store the first k numbers of the form a + b sqrt(2)
    cand = [Number(0,0)]

    i = j = 0
    for _ in range(1, k):
        cand_i_plus_1 = Number(cand[i].a + 1, cand[i].b)
        cand_j_plus_sqrt2 = Number(cand[j].a , cand[j].b + 1)
        cand.append(min(cand_i_plus_1, cand_j_plus_sqrt2))

        if cand_i_plus_1.val == cand[-1].val:
            i += 1
        if cand_j_plus_sqrt2.val == cand[-1].val:
            j += 1

    return [a.val for a in cand]

print(generate_first_k_a_b_sqrt2(5))