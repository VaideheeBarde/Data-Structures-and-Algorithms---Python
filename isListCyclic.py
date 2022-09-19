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

if __name__ == "__main__":
    L = LinkedList()
    L.append_node(4)
    L.append_node(2)
    L.append_node(3)
    L.append_node(1)

    L.head.next.next.next.next = L.head

    print(has_cycle(L.head))