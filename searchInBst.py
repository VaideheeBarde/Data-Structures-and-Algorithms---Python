class BstNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right

def search_bst(tree, key):
    return (tree if not tree or tree.data == key else search_bst(tree.left, key) if key < tree.data else search_bst(tree.right, key))

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

print(search_bst(a, 31))
print(search_bst(a, 12))