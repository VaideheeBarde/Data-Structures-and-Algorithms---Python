#Left subtree contains nodes with keys less than the node's key
#Right subtree contains only nodes with keys greater than node's key

class BstNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right

def is_binary_tree_bst(tree):

    def are_keys_in_range(tree, low_range=float('-inf'), high_range=float('inf')):
        if not tree:
            return True
        elif not low_range <= tree.data <= high_range:
            return False
        return (are_keys_in_range(tree.left, low_range, tree.data) and are_keys_in_range(tree.right, tree.data, high_range))

    return are_keys_in_range(tree)

m = BstNode(31)
l = BstNode(29, None, m)
n = BstNode(41)
k = BstNode(37, l, n)
p = BstNode(53)
j = BstNode(23, None, k)
o = BstNode(47, None, p)
i = BstNode(43, j, o)
h = BstNode(13)
g = BstNode(17, h)
d = BstNode(2)
e = BstNode(5)
c = BstNode(3, d, e)
f = BstNode(11, None, g)
b = BstNode(7, c, f)
a = BstNode(19, b, i)

print(is_binary_tree_bst(a))