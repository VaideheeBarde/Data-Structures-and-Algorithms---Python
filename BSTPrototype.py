class BstNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right

b = BstNode(2)
c = BstNode(3)
a = BstNode(1, b, c)

print(a.left.data)
print(a.right.data)