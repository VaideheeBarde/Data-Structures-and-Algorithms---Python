def lca(node0, node1):
    iter0, iter1 = node0, node1
    nodes_on_path_to_root = set()

    while iter0 or iter1:
        #Ascend tree in tandem for these two nodes

        if iter0:
            if iter0 in nodes_on_path_to_root:
                return iter0.data
            nodes_on_path_to_root.add(iter0)
            iter0 = iter0.parent

        if iter1:
            if iter1 in nodes_on_path_to_root:
                return iter1.data
            nodes_on_path_to_root.add(iter1)
            iter1 = iter1.parent

    raise ValueError('node0 and node1 are not in the same tree')

class BinaryTreeNode:
    def __init__(self, data=None, parent=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

root = BinaryTreeNode(314)

a = root.left = BinaryTreeNode(6)
b = root.right = BinaryTreeNode(6)
a.parent = b.parent = root

c = root.left.left = BinaryTreeNode(271)
d = root.left.right = BinaryTreeNode(561)
c.parent = d.parent = a

e = root.right.left = BinaryTreeNode(2)
f = root.right.right = BinaryTreeNode(271)
e.parent = f.parent = b

g = root.left.left.left = BinaryTreeNode(28)
h = root.left.left.right = BinaryTreeNode(0)
g.parent = h.parent = c

i = root.left.right.right = BinaryTreeNode(3)
i.parent = d

j = root.right.left.right = BinaryTreeNode(1)
j.parent = e

k = root.right.right.right = BinaryTreeNode(28)
k.parent = f

l = root.left.right.right.left = BinaryTreeNode(17)
l.parent = i

m = root.right.left.right.left = BinaryTreeNode(401)
n = root.right.left.right.right = BinaryTreeNode(257)
m.parent = n.parent = j

o = root.right.left.right.left.right = BinaryTreeNode(641)
o.parent = m

print(lca(h, l))
print(lca(g, h))
print(lca(l,b))