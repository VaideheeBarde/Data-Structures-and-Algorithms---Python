#leaves do not have children

def create_list_of_leaves(tree):
    if not tree:
        return []
    if not tree.left and not tree.right:
        return [tree.data]

    #First do the left subtree, and then do the right subtree
    return create_list_of_leaves(tree.left) + create_list_of_leaves(tree.right)

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

root = BinaryTreeNode(314)

root.left = BinaryTreeNode(6)
root.right = BinaryTreeNode(6)

root.left.left = BinaryTreeNode(271)
root.left.right = BinaryTreeNode(561)

root.right.left = BinaryTreeNode(2)
root.right.right = BinaryTreeNode(271)

root.left.left.left = BinaryTreeNode(28)
root.left.left.right = BinaryTreeNode(0)

root.left.right.right = BinaryTreeNode(3)

root.right.left.right = BinaryTreeNode(1)

root.right.right.right = BinaryTreeNode(28)

root.left.right.right.left = BinaryTreeNode(17)

root.right.left.right.left = BinaryTreeNode(401)
root.right.left.right.right = BinaryTreeNode(257)

root.right.left.right.left.right = BinaryTreeNode(641)

print(create_list_of_leaves(root))