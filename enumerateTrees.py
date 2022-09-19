class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def generate_all_binary_trees(num_nodes):
    if num_nodes == 0:
        return [None]

    result = []
    for num_left_tree_nodes in range(num_nodes):
        num_right_tree_nodes = num_nodes -1 - num_left_tree_nodes
        left_subtrees = generate_all_binary_trees(num_left_tree_nodes)
        right_subtrees = generate_all_binary_trees(num_right_tree_nodes)

        #Generates all combinations of left_subtrees and right subtrees
        result += [BinaryTreeNode(0, left, right) for left in left_subtrees for right in right_subtrees]

    return result

print(generate_all_binary_trees(3))