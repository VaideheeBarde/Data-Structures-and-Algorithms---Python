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

def has_cycle(head):
    def cycle_length(end):
        start, step = end, 0

        while True:
            step += 1
            start = start.next
            if start is end:
                return step

    fast = slow = head

    while fast and fast.next and fast.next.next:
        fast, slow = fast.next.next, slow.next

        if slow is fast:
            cycle_length_advanced_it = head

            for _ in range(cycle_length(slow)):
                cycle_length_advanced_it = cycle_length_advanced_it.next

            it = head

            while it is not cycle_length_advanced_it:
                it = it.next
                cycle_length_advanced_it = cycle_length_advanced_it.next

            return it.data

    return None

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

def overlapping_lists(l0, l1):
    root0, root1 = has_cycle(l0), has_cycle(l1)

    if not root0 and not root1:
        return overlapping_no_cycle_lists(l0, l1)

    elif (root0 and not root1) or (not root0 and root1):
        return None

    temp = root1
    while temp:
        temp = temp.next
        if temp is root0 or temp is root1:
            break

    return root1 if temp is root0 else None

if __name__ == "__main__":
    L1 = LinkedList()
    L1.append_node(1)
    L1.append_node(2)
    L1.append_node(3)
    L1.append_node(4)
    L1.head.next.next.next.next = L1.head

    L2 = LinkedList()
    L2.append_node(3)
    L2.append_node(4)
    L2.head.next = L1.head.next.next.next    

    print(overlapping_lists(L1.head, L2.head))