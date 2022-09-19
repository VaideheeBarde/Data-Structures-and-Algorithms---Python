class BstNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right

#Input nodes are non empty and the key at s is less than or equal to the key at b 
# => (s is left node and b is right node)

def find_lca(tree, s, b):
    while tree.data < s.data or tree.data > b.data:
        #Keep searching since tree is outside of [s, b]
        while tree.data < s.data:
            tree = tree.right
        while tree.data > b.data:
            tree = tree.left

    #Now s.data <= tree.data and b.data > tree.data
    return tree.data

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

print(find_lca(a, j, o))