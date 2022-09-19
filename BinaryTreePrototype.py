class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

#Implement 3 basic traversals - inorder, preorder, postorder

def tree_traversal(root):
    if root:
        #Preorder: processes the root before traversals of left and right children
        print('Preorder: %d' %root.data)
        tree_traversal(root.left)

        #Inorder: processes the root after traversal of the left child and before traversal of the right child
        print('Inorder: %d' %root.data)
        tree_traversal(root.right)

        #Postorder: Processes the root after the traversal of left and right
        print('Postorder: %d' %root.data)

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

print(tree_traversal(root))