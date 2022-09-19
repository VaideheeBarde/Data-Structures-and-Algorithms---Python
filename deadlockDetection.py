class GraphVertex:
    WHITE, GRAY, BLACK = range(3)

    def __init__(self):
        self.color = GraphVertex.WHITE
        self.edges = []

def is_deadlocked(graph):
    def has_cycle(cur):
        #Visiting a grey vertex means a cycle
        if cur.color == GraphVertex.GRAY:
            return True

        cur.color = GraphVertex.GRAY
        #Traverse the neighbour vertices
        if any(next.color != GraphVertex.BLACK and has_cycle(next) for next in cur.edges):
            return True

        cur.color = GraphVertex.BLACK #Marks current vertex as black
        return False

    return any(vertex.color == GraphVertex.WHITE and has_cycle(vertex) for vertex in graph)

#######Case 1########
a = GraphVertex()
b = GraphVertex()
c = GraphVertex()
d = GraphVertex()
e = GraphVertex()

a.edges = [b, c, d]
b.edges = [a, d, e]
c.edges = [a, d]
d.edges = [b, e]
e.edges = [b, d]

print(is_deadlocked([a, b, c, d, e]))

######Case 2#######
a = GraphVertex()
b = GraphVertex()
c = GraphVertex()

a.edges = [b, c]

print(is_deadlocked([a, b, c]))