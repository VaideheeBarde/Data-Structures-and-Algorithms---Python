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

def even_odd_merge(L):
    even_dummy_head, odd_dummy_head = Node(0), Node(0)
    tails, turn = [even_dummy_head, odd_dummy_head], 0

    while L:
        tails[turn].next = L
        L = L.next
        tails[turn] = tails[turn].next
        turn ^= 1 #Alternate between even and odd

    tails[1].next = None
    tails[0].next = odd_dummy_head.next

    return even_dummy_head.next

if __name__ == "__main__":
    L = LinkedList()
    #L.append_node(1)
    L.append_node(2)
    L.append_node(3)
    L.append_node(4)
    L.append_node(5)
    L.append_node(6)
    L.append_node(7)
    L.append_node(8)

#when L starts with odd number, the result list order is even followed by odd
#when L starts with even number, the result list order is odd followed by even

    test = LinkedList()
    test.head = even_odd_merge(L.head)
    test.print_list()