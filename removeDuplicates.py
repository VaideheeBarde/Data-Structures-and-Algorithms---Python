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

def remove_duplicates(L):
    it = L

    while it:
        #Uses next_distinct to find the next distinct value
        next_distinct = it.next

        while next_distinct and next_distinct.data == it.data:
            next_distinct = next_distinct.next

        it.next = next_distinct
        it = next_distinct

    return L

if __name__ == "__main__":
    L = LinkedList()
    L.append_node(1)
    L.append_node(2)
    L.append_node(2)
    L.append_node(3)
    L.append_node(4)
    L.append_node(4)

    test = LinkedList()
    test.head = remove_duplicates(L.head)
    test.print_list()