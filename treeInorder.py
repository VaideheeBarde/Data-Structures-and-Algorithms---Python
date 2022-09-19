def inorder_traversal(tree):
    result = []

    in_process = [(tree, False)]

    while in_process:
        node, left_subtree_traversed = in_process.pop()

        if node:
            if left_subtree_traversed:
                result.append(node.data)
            else:
                in_process.append((node.right, False))
                in_process.append((node, True))
                in_process.append((node.left, False))

    return result

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

root = BinaryTreeNode(314)

a = root.left = BinaryTreeNode(6)
b = root.right = BinaryTreeNode(6)

c = root.left.left = BinaryTreeNode(271)
d = root.left.right = BinaryTreeNode(561)

e = root.right.left = BinaryTreeNode(2)
f = root.right.right = BinaryTreeNode(271)

g = root.left.left.left = BinaryTreeNode(28)
h = root.left.left.right = BinaryTreeNode(0)

i = root.left.right.right = BinaryTreeNode(3)

j = root.right.left.right = BinaryTreeNode(1)

k = root.right.right.right = BinaryTreeNode(28)

l = root.left.right.right.left = BinaryTreeNode(17)

m = root.right.left.right.left = BinaryTreeNode(401)
n = root.right.left.right.right = BinaryTreeNode(257)

o = root.right.left.right.left.right = BinaryTreeNode(641)

print(inorder_traversal(a))