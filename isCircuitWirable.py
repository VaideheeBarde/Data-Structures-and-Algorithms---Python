import collections

class GraphVertex:
    def __init__(self):
        self.d = -1
        self.edges = []

def is_any_placement_feasible(graph):
    def bfs(s):
        s.d = 0
        q = collections.deque([s])

        while q:
            for t in q[0].edges:
                if t.d == -1:
                    t.d = q[0].d + 1
                    q.append(t)
                elif t.d == q[0].d:
                    return False
                
            del q[0]

        return True

    return all(bfs(v) for v in graph if v.d == -1)

a = GraphVertex()
b = GraphVertex()
c = GraphVertex()
d = GraphVertex()
e = GraphVertex()
f = GraphVertex()
g = GraphVertex()
h = GraphVertex()
i = GraphVertex()
j = GraphVertex()
k = GraphVertex()
l = GraphVertex()
m = GraphVertex()
n = GraphVertex()
o = GraphVertex()
p = GraphVertex()
q = GraphVertex()
r = GraphVertex()
s = GraphVertex()
t = GraphVertex()
u = GraphVertex()
v = GraphVertex()

a.edges = [b, c]
b.edges = [a, g, e]
c.edges = [a, d, e]
d.edges = [c, f]
e.edges = [b, f, c, h]
f.edges = [d, i, e]
g.edges = [b, h, j]
h.edges = [e, g, k, i]
i.edges = [f, h, l]
j.edges = [g, m, k]
k.edges = [j, n, l]
l.edges = [i, o, k]
m.edges = [j, n]
n.edges = [m, k, q, p]
o.edges = [l, r]
p.edges = [n, s]
q.edges = [n, s, r]
r.edges = [o, t, q]
s.edges = [p, u, q]
t.edges = [r, v]
u.edges = [s, v]
v.edges = [u, t, q]

print(is_any_placement_feasible([a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v]))