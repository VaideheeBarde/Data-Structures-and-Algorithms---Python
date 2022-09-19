class Queue:
    def __init__(self):
        self._enq = []
        self._deq = []

    def enqueue(self, x):
        self._enq.append(x)

    def dequeue(self):
        if not self._deq:
            #Transfers the elements in _enq to _deq
            while self._enq:
                self._deq.append(self._enq.pop())
        return self._deq.pop()

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
