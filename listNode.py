class ListNode:
    def __init__(self, data=0, next=None, head=None):
        self.data = data
        self.next = next
        self.head = head
        
    def search_list(self, L, key):
        while L and L.data!=key:
            L = L.next
        return L.data

    def insert_after(self, new_node, node):
        new_node.next = node.next
        node.next = new_node

    def delete_after(self,node):
        node.next=node.next.next

    def pushList(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def append(self, new_data): 
        new_node = ListNode(new_data) 
          
        if self.head is None: 
            self.head = new_node 
            return
            
        last = self.head 
        while last.next: 
            last = last.next
        last.next = new_node 

    def count_nodes(self):
        tail, n= L, 0

        while tail:
            n += 1
            tail = tail.next
        
        return n

track = ListNode()

a=ListNode(1)
b=ListNode(2)
c=ListNode(3)

a.next=b
b.next=c

print(a.next.data)
print(b.next.data)

d=ListNode(4)
track.insert_after(d, c)
print(c.next.data)

track.delete_after(c)
#print(c.next.data)
print("")
track.head=a
track.printList()
print("")
L = a
print(track.search_list(L, 2))
print("")
L1 = ListNode()
L1.pushList(1)
L1.pushList(2)
L1.pushList(4)
L1.printList()

print(L1.count_nodes())