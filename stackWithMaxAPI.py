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

s = Stack()
print(s.empty())
s.push(-1)
s.push(-2)
s.push(-5)
s.push(-6)
s.push(-3)
s.push(-4)
s.push(-1)
print(s.empty())
print(s.pop())
print(s.max())