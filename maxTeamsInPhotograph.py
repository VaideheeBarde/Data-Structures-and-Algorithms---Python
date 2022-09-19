#Runs on terminal - python 3 for no edges defined. Throws recursion depth for others.

class GraphVertex:
    def __init__(self):
        self.edges = []
        #Set max_distance = 0 to indicate unvisited vertex
        self.max_distance = 0

def find_largest_number_teams(graph):
    def dfs(curr):
        curr.max_distance = max(((vertex.max_distance if vertex.max_distance != 0 else dfs(vertex)) + 1 for vertex in curr.edges), default=1)
        return curr.max_distance

    return max(dfs(g) for g in graph if g.max_distance == 0)

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

print(find_largest_number_teams([a, b, c, d, e]))