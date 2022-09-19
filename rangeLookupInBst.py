import collections

Interval = collections.namedtuple('Interval', ('left', 'right'))

class BstNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right

def range_lookup_in_bst(tree, interval):
    def range_lookup_in_bst_helper(tree):
        if tree is None:
            return None

        if interval.left <= tree.data <= interval.right:
            range_lookup_in_bst_helper(tree.left)
            result.append(tree.data)
            range_lookup_in_bst_helper(tree.right)

        elif interval.left > tree.data:
            range_lookup_in_bst_helper(tree.right)

        else:
            range_lookup_in_bst_helper(tree.left)

    result = []
    range_lookup_in_bst_helper(tree)
    return result

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

interval = Interval(16, 31)
print(range_lookup_in_bst(a, interval))