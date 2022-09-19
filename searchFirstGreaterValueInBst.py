class BstNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right

def find_first_greater_than_k(tree, k):
    subtree, first_so_far = tree, None
    while subtree:
        if subtree.data > k:
            first_so_far, subtree = subtree, subtree.left
        else:
            subtree = subtree.right
    return first_so_far.data

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

print(find_first_greater_than_k(a, 23))