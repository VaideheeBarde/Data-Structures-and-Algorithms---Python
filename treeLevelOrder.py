def binary_tree_depth_order(tree):
    result = []
    if not tree:
        return result

    curr_depth_nodes = [tree]
    
    while curr_depth_nodes:
        result.append([curr.data for curr in curr_depth_nodes])
        curr_depth_nodes = [child for curr in curr_depth_nodes for child in (curr.left, curr.right) if child]

    return result

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

root = Node(314)

root.left = Node(6)
root.right = Node(6)

root.left.left = Node(271)
root.left.right = Node(561)

root.right.left = Node(2)
root.right.right = Node(271)

root.left.left.left = Node(28)
root.left.left.right = Node(0)

root.left.right.right = Node(3)

root.right.left.right = Node(1)

root.right.right.right = Node(28)

root.left.right.right.left = Node(17)

root.right.left.right.left = Node(401)
root.right.left.right.right = Node(257)

root.right.left.right.left.right = Node(641)

print(binary_tree_depth_order(root))