class BstNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right

def find_k_largest_in_bst(tree, k):
    def find_k_largest_in_bst_helper(tree):
        if tree and len(k_largest_elements) < k:
            find_k_largest_in_bst_helper(tree.right)
            if len(k_largest_elements) < k:
                k_largest_elements.append(tree.data)
                find_k_largest_in_bst_helper(tree.left)

    k_largest_elements = []
    find_k_largest_in_bst_helper(tree)
    return k_largest_elements

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

print(find_k_largest_in_bst(a, 3))