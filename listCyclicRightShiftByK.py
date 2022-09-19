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

def cyclic_right_shift_by_k(L, k):
    if L is None:
        return L

    tail, n = L, 1

    while tail.next:
        n += 1
        tail = tail.next

    k %= n
    if k == 0:
        return L

    tail.next = L
    steps_to_new_head, new_tail = n-k, tail

    while steps_to_new_head:
        steps_to_new_head -= 1
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None

    return new_head

if __name__ == "__main__":
    L = LinkedList()
    L.append_node(1)
    L.append_node(2)
    L.append_node(3)
    L.append_node(4)
    L.append_node(5)
    L.append_node(6)
    L.append_node(7)

    test = LinkedList()
    test.head = cyclic_right_shift_by_k(L.head, 2)
    test.print_list()