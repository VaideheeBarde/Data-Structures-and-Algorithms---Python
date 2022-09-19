import collections

def lca(tree, node0, node1):
    Status = collections.namedtuple('Status', ('num_target_nodes', 'ancestor'))

    #Returns an object consisting of an int and a node
    #The int field is 0, 1 or 2 depending on how many of {node0, node1} are present in the tree
    #If both are present in the tree, when ancestor is assigned to a non-null value, it is the LCA

    def lca_helper(tree, node0, node1):
        #Base case
        if tree is None:
            return Status(0, None)

        left_result = lca_helper(tree.left, node0, node1)
        if left_result.num_target_nodes == 2:
            #Found both nodes in the left subtree
            return left_result

        right_result = lca_helper(tree.right, node0, node1)
        if right_result.num_target_nodes == 2:
            #Found both nodes in the right subtree
            return right_result

        num_target_nodes = (left_result.num_target_nodes + right_result.num_target_nodes + (node0, node1).count(tree))
        return Status(num_target_nodes, tree if num_target_nodes == 2 else None)

    return lca_helper(tree, node0, node1).ancestor.data

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

print(lca(root, l, o))
print(lca(root, m, n))