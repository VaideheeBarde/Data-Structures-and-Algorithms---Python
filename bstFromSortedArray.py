class BstNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right

def build_min_height_bst_from_sorted_array(A):
    def build_min_height_bst_from_sorted_subarray(start, end):
        if start >= end:
            return None

        mid = (start + end) // 2

        return BstNode(A[mid], build_min_height_bst_from_sorted_subarray(start, mid), build_min_height_bst_from_sorted_subarray(mid+1, end))

    return build_min_height_bst_from_sorted_subarray(0, len(A))

A = [2,3,5,7,11,13,17,19,23]
print(build_min_height_bst_from_sorted_array(A))