#Assumes node to delete is not tail

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def deletion_of_node(node_to_delete):
    node_to_delete.data = node_to_delete.next.data
    node_to_delete.next = node_to_delete.next.next

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

deletion_of_node(b)

print(a.next.data)