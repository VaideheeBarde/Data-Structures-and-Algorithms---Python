import collections

Item = collections.namedtuple('Item', ('weight', 'value'))

def optimum_subject_to_capacity(items, capacity):
    def optimum_subject_to_item_and_capacity(k, available_capacity):
        if k < 0:
            return 0

        if V[k][available_capacity] == -1:
            without_curr_item = optimum_subject_to_item_and_capacity(k-1, available_capacity)
            with_curr_item = (0 if available_capacity < items[k].weight else (items[k].value + optimum_subject_to_item_and_capacity(k-1, available_capacity - items[k].weight)))
            V[k][available_capacity] = max(without_curr_item, with_curr_item)

        return V[k][available_capacity]

    V = [[-1] * (capacity+1) for _ in items]
    return optimum_subject_to_item_and_capacity(len(items) - 1, capacity)

items = []
A = Item(20, 65)
B = Item(8, 35)
C = Item(60, 245)
D = Item(55, 195)
E = Item(40, 65)
F = Item(70, 150)
G = Item(85, 275)
H = Item(25, 155)
I = Item(30, 120)
J = Item(65, 320)
K = Item(75, 75)
L = Item(10, 40)
M = Item(95, 200)
N = Item(50, 100)
O = Item(40, 220)
P = Item(10, 99)

items.append(A)
items.append(B)
items.append(C)
items.append(D)
items.append(E)
items.append(F)
items.append(G)
items.append(H)
items.append(I)
items.append(J)
items.append(K)
items.append(L)
items.append(M)
items.append(N)
items.append(O)
items.append(P)

print(items)
print(optimum_subject_to_capacity(items, 130))