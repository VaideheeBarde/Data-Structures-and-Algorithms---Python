def inorder_traversal(tree):
    prev, result = None, []
    while tree:
        if prev is tree.parent:
            #We came down to tree from previous
            if tree.left: #Keep going left
                next = tree.left
            else:
                result.append(tree.data)
                #Done with left, so go right if right is not empty
                #Otherwise, go up
                next = tree.right or tree.parent

        elif tree.left is prev:
            #We came up to tree from its left child
            result.append(tree.data)
            #Done with left, so go right if right is not empty.
            #Otherwise, go up
            next = tree.right or tree.parent
        else: #Done with both children, so move up
            next = tree.parent

        prev, tree = tree, next

    return result

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

print(inorder_traversal(root))