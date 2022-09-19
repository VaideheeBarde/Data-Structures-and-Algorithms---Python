class A():
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return isinstance(other, A) and self.x == other.x

    def __hash__(self):
        return self.x * 113 + 119

u = A(42)
v = A(42)
U = (u, )
V = (v, )
S = set([U])
print(U in S)
print(V in S)
u.x = 28
print(U in S)