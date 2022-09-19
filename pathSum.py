def has_path_sum(tree, remaining_weight):
    if not tree:
        return False

    #Leaf
    if not tree.left and not tree.right: 
        return remaining_weight == tree.data 

    #Non Leaf
    return (has_path_sum(tree.left, remaining_weight-tree.data) or has_path_sum(tree.right, remaining_weight-tree.data))

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

print(has_path_sum(root, 591))