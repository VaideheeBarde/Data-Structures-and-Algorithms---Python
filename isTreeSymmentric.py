def is_symmetric(tree):
    def check_symmetric(subtree_0, subtree_1):
        #Base Case
        if not subtree_0 and not subtree_1:
            return True
        elif subtree_0 and subtree_1:
            return (subtree_0.data == subtree_1.data and check_symmetric(subtree_0.left, subtree_1.right) and check_symmetric(subtree_0.right, subtree_1.left))
        return False
    
    return not tree or check_symmetric(tree.left, tree.right)

class BinaryNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

root = BinaryNode(1)
root.left = BinaryNode(2)
root.right = BinaryNode(2)

root.left.left = BinaryNode(1)
root.left.right = BinaryNode(2)

root.right.right = BinaryNode(1)
root.right.left = BinaryNode(2)

print(is_symmetric(root))