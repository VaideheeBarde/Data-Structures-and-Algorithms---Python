def sum_root_to_leaf(tree):
    def sum_root_to_leaf_helper(tree, partial_path_sum = 0):
        if not tree:
            return 0

        partial_path_sum = partial_path_sum * 2 + tree.data

        if not tree.left and not tree.right:
            return partial_path_sum

        #Non-leaf

        return(sum_root_to_leaf_helper(tree.left, partial_path_sum) + sum_root_to_leaf_helper(tree.right, partial_path_sum))

    return sum_root_to_leaf_helper(tree)

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

a = BinaryTreeNode(1)
b = BinaryTreeNode(0)
i = BinaryTreeNode(1)
a.left = b
a.right = i
c = BinaryTreeNode(0)
f = BinaryTreeNode(1)
b.left = c
b.right = f
d = BinaryTreeNode(0)
e = BinaryTreeNode(1)
c.left = d
c.right = e
g = BinaryTreeNode(1)
f.right = g
h = BinaryTreeNode(0)
g.left = h
j = BinaryTreeNode(0)
o = BinaryTreeNode(0)
i.left = j
i.right = o
k = BinaryTreeNode(0)
j.right = k
l = BinaryTreeNode(1)
n = BinaryTreeNode(0)
k.left = l
k.right = n
m = BinaryTreeNode(1)
l.right = m
p = BinaryTreeNode(0)
o.right = p

print(sum_root_to_leaf(i))