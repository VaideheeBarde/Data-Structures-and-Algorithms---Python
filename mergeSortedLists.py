class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head = None):
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

def merge_sorted_lists(head1, head2):
    dummyhead = tail = Node()

    while head1 and head2:
        if head1.data < head2.data:
            tail.next = head1
            head1 = head1.next

        else:
            tail.next = head2
            head2 = head2.next

        tail = tail.next

    tail.next = head1 or head2

    return dummyhead.next

if __name__ == "__main__":
    L1 = LinkedList()
    L1.append_node(10)
    L1.append_node(20)
    L1.append_node(30)

    L2 = LinkedList()
    L2.append_node(5)
    L2.append_node(10)
    L2.append_node(15)

    test = LinkedList()
    test.head = merge_sorted_lists(L1.head, L2.head)
    test.print_list()