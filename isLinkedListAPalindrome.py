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

def reverse_list(L):
    dummy_head = sublist_head = Node(0, L)
    
    sublist_iter = sublist_head.next
   
    n = 0
    node = L
    while node:
        n+=1
        node = node.next

    for _ in range(n-1):
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp

    return dummy_head.next

def check_palindromic(L):
    fast = slow = L

    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

    first_half_iter, second_half_iter = L, reverse_list(slow)

    while first_half_iter and second_half_iter:
        if first_half_iter.data != second_half_iter.data:
            return False
        first_half_iter, second_half_iter = first_half_iter.next, second_half_iter.next

    return True

if __name__ == "__main__":
    L = LinkedList()
    L.append_node(1)
    L.append_node(2)
    L.append_node(2)
    L.append_node(1)
    #L.print_list()

    print(check_palindromic(L.head))