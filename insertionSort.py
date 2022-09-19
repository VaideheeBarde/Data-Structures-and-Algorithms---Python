class ListNode:
    def __init__(self, data=0, next=None, head = None):
        self.data = data
        self.next = next
        self.head = head

def insertion_sort(L):
    dummy_head = ListNode(0, L)

    while L and L.next:
        if L.data > L.next.data:
            target, pre = L.next, dummy_head
            while pre.next.data < target.data:
                pre = pre.next
            temp, pre.next, L.next = pre.next, target, target.next
            target.next = temp
        else:
            L = L.next
        
    return dummy_head.next.data

L1 = ListNode(5)
L2 = ListNode(4)
L3 = ListNode(5)
L4 = ListNode(6)
L5 = ListNode(7)

L1.next = L2
L2.next = L3
L3.next = L4
L4.next = L5

print(insertion_sort(L1))