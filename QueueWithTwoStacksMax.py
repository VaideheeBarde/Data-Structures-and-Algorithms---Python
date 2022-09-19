import collections
from collections import namedtuple

class Stack:
    ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax', ('element', 'max'))

    def __init__(self):
        self._element_with_cached_max = []

    def empty(self):
        return len(self._element_with_cached_max) == 0

    def max(self):
        return self._element_with_cached_max[-1].max

    def pop(self):
        return self._element_with_cached_max.pop().element

    def push(self, x):
        self._element_with_cached_max.append(self.ElementWithCachedMax(x, x if self.empty() else max(x, self.max())))


class QueueWithMax:
    def __init__(self):
        self._enqueue = Stack()
        self._dequeue = Stack()

    def enqueue(self, x):
        self._enqueue.push(x)

    def dequeue(self):
        if self._dequeue.empty():
            while not self._enqueue.empty():
                self._dequeue.push(self._enqueue.pop())

        return self._dequeue.pop()

    def max(self):
        if not self._enqueue.empty():
            return self._enqueue.max() if self._dequeue.empty() else max(self._enqueue.max(), self._dequeue.max())
        return self._dequeue.max()

q = QueueWithMax()
q.enqueue(5)
q.enqueue(4)
q.enqueue(3)
q.enqueue(2)
q.enqueue(1)

print(q.max())

q.dequeue()
q.dequeue()
q.dequeue()
print(q.max())