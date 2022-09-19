#Given a binary tree, find the nth node in inorder traversal

def find_kth_node_in_binary_tree(tree, k):
    while tree:
        left_size = tree.left.size if tree.left else 0
        
        if left_size + 1 < k: #k-th node must be in the right subtree
            k -= left_size + 1
            tree = tree.right 
        elif left_size == k-1: #k-th is iter itself
            return tree.data
        else: #k-th node must be in left subtree of iter
            tree = tree.left
            
    return None  #If k is between 1

def get_size(node): 
    if node is None: 
        return 0 
    else: 
        return (get_size(node.left)+ 1 + get_size(node.right)) 


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, size=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = size

root = BinaryTreeNode(1)

a = root.left = BinaryTreeNode(2)
b = root.right = BinaryTreeNode(3)

c = a.left = BinaryTreeNode(4)
d = a.right = BinaryTreeNode(5)

e = b.left = BinaryTreeNode(6)
f = b.right = BinaryTreeNode(7)

g = c.left = BinaryTreeNode(8)
h = c.right = BinaryTreeNode(9)

i = d.left = BinaryTreeNode(10)
j = d.right = BinaryTreeNode(11)

k = e.left = BinaryTreeNode(12)

l = f.right = BinaryTreeNode(13)

root.size = get_size(root)
a.size = get_size(a)
b.size = get_size(b)
c.size = get_size(c)
d.size = get_size(d)
e.size = get_size(e)
f.size = get_size(f)
g.size = get_size(g)
h.size = get_size(h)
i.size = get_size(i)
j.size = get_size(j)
k.size = get_size(k)
l.size = get_size(l)

print(find_kth_node_in_binary_tree(root, 1))
print(find_kth_node_in_binary_tree(root, 2))
print(find_kth_node_in_binary_tree(root, 3))
print(find_kth_node_in_binary_tree(root, 4))
print(find_kth_node_in_binary_tree(root, 5))
print(find_kth_node_in_binary_tree(root, 6))
print(find_kth_node_in_binary_tree(root, 7))
print(find_kth_node_in_binary_tree(root, 8))
print(find_kth_node_in_binary_tree(root, 9))
print(find_kth_node_in_binary_tree(root, 10))
print(find_kth_node_in_binary_tree(root, 11))
print(find_kth_node_in_binary_tree(root, 12))
print(find_kth_node_in_binary_tree(root, 13))
print(find_kth_node_in_binary_tree(root, 14))