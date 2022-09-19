class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def insert_after(new_node, node):
    new_node.next = node.next
    node.next = new_node

def delete_after(node):
    node.next = node.next.next

def search_in_list(L, key):
    while L and L.data != key:
        L = L.next
    return L    
    
def reverse_sublist(L, start, finish):
    dummy_head = sublist_head = ListNode(0, L)

    for _ in range(1, start):
        sublist_head = sublist_head.next

    sublist_iter = sublist_head.next

    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = (temp.next, sublist_head.next, temp)

    return dummy_head.next.next.next.next.next.data

e = ListNode(2)
d = ListNode(7, e)
c = ListNode(5, d)
b = ListNode(3, c)
a = ListNode(11, b)


print(reverse_sublist(a, 3, 5))
#11,3,2,7,5