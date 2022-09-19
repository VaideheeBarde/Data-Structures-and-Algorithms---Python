#Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append_node(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def print_list(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next

def list_pivoting(l, x):
    less_head = less_iter = Node()
    equal_head = equal_iter = Node()
    greater_head = greater_iter = Node()

    while l:
        if l.data < x:
            less_iter.next = l
            less_iter = less_iter.next

        elif l.data == x:
            equal_iter.next = l
            equal_iter = equal_iter.next

        else:
            greater_iter.next = l
            greater_iter = greater_iter.next

        l = l.next

    greater_iter.next = None
    equal_iter.next = greater_head.next
    less_iter.next = equal_head.next

    return less_head.next

if __name__ == "__main__":
    L = LinkedList()
    L.append_node(1)
    L.append_node(6)
    L.append_node(2)
    L.append_node(5)
    L.append_node(3)
    L.append_node(4)
    L.append_node(4)

    test = LinkedList()
    test.head = list_pivoting(L.head, 4)
    test.print_list()