def lca(node0, node1):

    def get_depth(node):

        depth = 0

        while node:
            depth += 1
            node = node.parent
        return depth

    depth0, depth1 = map(get_depth, (node0, node1))

    #Makes node0 as the deeper node in order to simplify the code
    if depth1 > depth0:
        node0, node1 = node1, node0

    #Ascends from the deeper node
    depth_diff = abs(depth0 - depth1) 
    while depth_diff:
        node0 = node0.parent
        depth_diff -= 1

    #Now ascends both nodes until we reach the LCA
    while node0 is not node1:
        node0, node1 = node0.parent, node1.parent

    return node0.data   

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

print(lca(l, h))