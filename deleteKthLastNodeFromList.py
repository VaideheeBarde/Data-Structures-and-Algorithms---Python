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

def remove_kth_last_node_from_list(L, k):
    dummy_head = Node(0, L)

    first = dummy_head.next

    for _ in range(k):
        first = first.next

    second = dummy_head

    while first:
        first = first.next
        second = second.next

    second.next = second.next.next
    return dummy_head.next

if __name__ == "__main__":
    list1 = LinkedList()
    list1.append_node(1)
    list1.append_node(2)
    list1.append_node(3)
    list1.append_node(4)
    list1.append_node(5)
    list1.append_node(6)

    test = LinkedList()
    test.head = remove_kth_last_node_from_list(list1.head, 3)
    test.print_list()