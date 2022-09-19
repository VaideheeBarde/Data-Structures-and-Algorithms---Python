#In Binary Tree, Inorder successor of a node is the next node in Inorder traversal of the Binary Tree

def find_successor(node):
    if node.right:
        #successor is the leftmose element in the node's right subtree
        node = node.right

        while node.left:
            node = node.left
        return node.data

    #Find the closest ancestor whose left subtree contains node
    while node.parent and node.parent.right is node:
        node = node.parent

    #A return value of None means node does not have a successor, i.e., node is the rightmost node in the tree
    return node.parent.data

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

print(find_successor(root))
print(find_successor(a))
print(find_successor(b))
print(find_successor(c))
print(find_successor(d))
print(find_successor(e))
print(find_successor(f))
print(find_successor(g))
print(find_successor(h))
print(find_successor(i))
print(find_successor(j))
#print(find_successor(k))
print(find_successor(l))
print(find_successor(m))
print(find_successor(n))
print(find_successor(o))