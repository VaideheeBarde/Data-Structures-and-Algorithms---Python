import collections

class GraphVertex:
    def __init__(self, label):
        self.label = label
        self.edges = []

def clone_graph(graph):
    if graph is None:
        return None

    q = collections.deque([graph])
    vertex_map = {graph: GraphVertex(graph.label)}

    while q:
        v = q.popleft()
        for e in v.edges:
            #Try to copy vertex e
            if e not in vertex_map:
                vertex_map[e] = GraphVertex(e.label)
                q.append(e)
            #Copy edge

            vertex_map[v].edges.append(vertex_map[e])

    return vertex_map[graph]

a = GraphVertex(1)
b = GraphVertex(2)
c = GraphVertex(3)
d = GraphVertex(4)
e = GraphVertex(5)

a.edges = [b, c, d]
b.edges = [a, d, e]
c.edges = [a, d]
d.edges = [b, e]
e.edges = [b, d]

print(clone_graph(b))