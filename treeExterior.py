def exterior_binary_tree(tree):

    #Compute nodes from root to leftmost leaf
    def left_boundary(subtree):
        if not subtree or (not subtree.left and not subtree.right):
            return

        exterior.append(subtree.data)

        if subtree.left:
            left_boundary(subtree.left)
        else:
            left_boundary(subtree.right)

    #Compute the nodes from rightmost leaf to root
    def right_boundary(subtree):
        if not subtree or (not subtree.left and not subtree.right):
            return

        if subtree.right:
            right_boundary(subtree.right)
        else:
            right_boundary(subtree.left)
        
        exterior.append(subtree.data)

    #Compute the leaves in left to right order
    def leaves(subtree):

        if not subtree:
            return
        if not subtree.left and not subtree.right:
            exterior.append(subtree.data)
            return
        
        leaves(subtree.left)
        leaves(subtree.right)

    if not tree:
        return []

    exterior = [tree.data]
    left_boundary(tree.left)
    leaves(tree.left)
    leaves(tree.right)
    right_boundary(tree.right)
    return exterior

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

"""
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
"""

root = BinaryTreeNode("A")

root.left = BinaryTreeNode("B")
root.right = BinaryTreeNode("C")

root.left.left = BinaryTreeNode("D")
root.left.right = BinaryTreeNode("E")

root.right.left = BinaryTreeNode("F")
root.right.right = BinaryTreeNode("G")

root.left.left.left = BinaryTreeNode("H")
root.left.left.right = BinaryTreeNode("I")

root.left.right.right = BinaryTreeNode("J")

root.right.left.right = BinaryTreeNode("K")

root.right.right.right = BinaryTreeNode("L")

root.left.right.right.left = BinaryTreeNode("M")

root.right.left.right.left = BinaryTreeNode("N")
root.right.left.right.right = BinaryTreeNode("O")

root.right.left.right.left.right = BinaryTreeNode("P")

print(exterior_binary_tree(root))