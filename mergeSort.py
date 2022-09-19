class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def append_node(self, new_data):
        new_node = ListNode(new_data)

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

def merge_two_sorted_lists(L1, L2):
    dummyhead = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next = L1
            L1 = L1.next

        else:
            tail.next = L2
            L2 = L2.next

        tail = tail.next

    tail.next = L1 or L2

    return dummyhead.next

def stable_sort_list(L):
    #Base cases: L is empty or a single node, nothing to do
    if L is None or L.next is None:
        return L

    #Find the midpoint of L using a slow and a fast pointer
    pre_slow, slow, fast = None, L, L
    while fast and fast.next:
        pre_slow = slow
        fast, slow = fast.next.next, slow.next

    if pre_slow:
        pre_slow.next = None #Splits the list into two equal sized lists

    return merge_two_sorted_lists(stable_sort_list(L), stable_sort_list(slow))

if __name__ == "__main__":
    L1 = LinkedList()
    L1.append_node(10)
    L1.append_node(20)
    L1.append_node(30)
    L1.append_node(5)
    L1.append_node(10)
    L1.append_node(15)

    test = LinkedList()
    test.head = stable_sort_list(L1.head)
    test.print_list()