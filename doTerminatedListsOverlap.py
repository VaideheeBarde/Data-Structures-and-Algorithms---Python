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

def overlapping_no_cycle_lists(l0, l1):
    def length(L):
        length = 0
        while L:
            length += 1
            L = L.next
        return length

    l0_len, l1_len = length(l0), length(l1)

    if l0_len > l1_len:
        l0, l1 = l1, l0

    for _ in range(abs(l0_len - l1_len)):
        l1 = l1.next

    while l0 and l1 and l0 is not l1:
        l0, l1 = l0.next, l1.next

    return l0

if __name__ == "__main__":
    L1 = LinkedList()
    L1.append_node(1)
    L1.append_node(2)
    L1.append_node(3)
    L1.append_node(4)

    L2 = LinkedList()
    L2.append_node(1)
    L2.append_node(3)

    print(overlapping_no_cycle_lists(L1.head, L2.head))