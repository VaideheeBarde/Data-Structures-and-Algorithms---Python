import collections

Subarray = collections.namedtuple('Subarray', ('left', 'right'))

def find_smallest_subarray_covering_set(paragraph, keywords):
    class DoublyLinkedListNode:
        def __init__(self, data=None):
            self.data = data
            self.next = self.prev = None

    class LinkedList:
        def __init__(self):
            self.head = self.tail = None
            self._size = 0

        def __len__(self):
            return self._size

        def insert_after(self, value):
            node = DoublyLinkedListNode(value)
            node.prev = self.tail
            if self.tail:
                self.tail.next = node
            else:
                self.head = node
            self.tail = node
            self._size += 1

        def remove(self, node):
            if node.next:
                node.next.prev = node.prev
            else:
                self.tail = node.prev
            if node.prev:
                node.prev.next = node.next
            else:
                self.head = node.next
            node.next = node.prev = None
            self._size -= 1

    #Tracks the last occurrence (index) of each string in keywords
    loc = LinkedList()
    print('init')
    print(len(loc))
    d = {s: None for s in keywords}
    result = Subarray(-1, -1)

    for idx, s in enumerate(paragraph):
        if s in d:
            it = d[s]
            
            if it is not None:
                loc.remove(it)
                
            loc.insert_after(idx)
            d[s] = loc.tail

            if len(loc) == len(keywords):
                if (result == (-1, -1) or idx - loc.head.data < result[1] - result[0]):
                    result = Subarray(loc.head.data, idx)

    return result

paragraph = ['apple', 'banana', 'apple', 'apple', 'dog', 'cat', 'apple', 'dog', 'banana', 'apple', 'cat', 'dog', 'banana']
keywords = ('banana', 'cat')

print(find_smallest_subarray_covering_set(paragraph, keywords))