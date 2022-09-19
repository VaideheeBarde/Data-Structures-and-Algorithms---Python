class BstNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right

def rebuild_bst_from_preorder(preorder_sequence):
    if not preorder_sequence:
        return None

    transition_point = next((i for i, a in enumerate(preorder_sequence) if a > preorder_sequence[0]), len(preorder_sequence))

    return BstNode(preorder_sequence[0], rebuild_bst_from_preorder(preorder_sequence[1:transition_point]), rebuild_bst_from_preorder(preorder_sequence[transition_point:]))

print(rebuild_bst_from_preorder([43, 23, 37, 29, 31, 47, 53]))