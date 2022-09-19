#Balanced binary tree - 
#for each node in the tree, the difference in the heights of left and right subtree is not more than 1

import collections

def is_balanced_binary_tree(tree):
    BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))
    #First value: indicates if tree is balanced
    #Second value: height of the tree

    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1) #Base Case

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            #left subtree is not balanced
            return BalancedStatusWithHeight(False, 0)

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            #right subtree is not balanced
            return BalancedStatusWithHeight(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)

    return check_balanced(tree).balanced
    #return check_balanced(tree).height

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

#root.right.right.right = BinaryTreeNode(28)

#root.left.right.right.left = BinaryTreeNode(17)

#root.right.left.right.left = BinaryTreeNode(401)
#root.right.left.right.right = BinaryTreeNode(257)

#root.right.left.right.left.right = BinaryTreeNode(641)

print(is_balanced_binary_tree(root))