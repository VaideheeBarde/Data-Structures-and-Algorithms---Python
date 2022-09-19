class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = None

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

def add_two_numbers(L1, L2):
    dummy_head = place_iter = Node()
    carry = 0

    while L1 or L2 or carry:
        val = carry + (L1.data if L1 else 0) + (L2.data if L2 else 0)
        L1 = L1.next if L1 else None
        L2 = L2.next if L2 else None
        place_iter.next = Node(val%10)
        place_iter, carry = place_iter.next, val//10

    return dummy_head.next

if __name__ == "__main__":
    L1 = LinkedList()
    L1.append_node(1)
    L1.append_node(6)
    L1.append_node(2)
    L1.append_node(9)

    L2 = LinkedList()
    L2.append_node(5)
    L2.append_node(3)
    L2.append_node(4)
    L2.append_node(4)

    test = LinkedList()
    test.head = add_two_numbers(L1.head, L2.head)
    test.print_list()