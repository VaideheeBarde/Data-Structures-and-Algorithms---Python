class BstNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right

def rebuild_bst_from_preorder(preorder_sequence):
    def rebuild_bst_from_preorder_on_value_range(lower_bound, upper_bound):
        if root_idx[0] == len(preorder_sequence):
            return None

        root = preorder_sequence[root_idx[0]]

        if not lower_bound <= root <= upper_bound:
            return None

        root_idx[0] += 1
        #Note that rebuild_bst_from_preorder_on_value_range updates root_idx[0]
        #So the order of following two calls are critical
        left_subtree = rebuild_bst_from_preorder_on_value_range(lower_bound, root)
        right_subtree = rebuild_bst_from_preorder_on_value_range(root, upper_bound)
        return BstNode(root, left_subtree, right_subtree)

    root_idx = [0] #Tracks current subtree
    return rebuild_bst_from_preorder_on_value_range(float('-inf'), float('inf'))

print(rebuild_bst_from_preorder([43, 23, 37, 29, 31, 47, 53]))