#Detect the right sibling of each node; for a right node, the right sibling will be its parent's right sibling's left child

def construct_right_sibling(tree):

    def populate_children_next_field(start_node):
        while start_node and start_node.left:
            #Populate left child's next field
            start_node.left.next = start_node.right
            #Populate right child's next field if start node is not the last node of level
            start_node.right.next = start_node.next and start_node.next.left
            start_node = start_node.next

    while tree and tree.left:
        populate_children_next_field(tree)
        tree = tree.left

class BinaryNode:
    def __init__(self, data=None, left=None, right=None, next=None):
        self.data = data
        self.left = left
        self.right = right
        self.next = next

root = BinaryNode(1)

root.left = BinaryNode(3)
root.right = BinaryNode(3)

root.left.left = BinaryNode(1)
root.left.right = BinaryNode(2)

root.right.right = BinaryNode(1)
root.right.left = BinaryNode(2)

print(construct_right_sibling(root))