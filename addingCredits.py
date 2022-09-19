import bintrees

class ClientsCreditInfo:
    def __init__(self):
        self._offset = 0
        self._client_to_credit = {}
        self._credit_to_clients = bintrees.RBTree()

    def insert(self, client_id, c):
        self.remove(client_id)
        self._client_to_credit[client_id] = c - self._offset
        self._credit_to_clients.set_default(c - self._offset, set()).add(client_id)

    def remove(self, client_id):
        credit = self._client_to_credit.get(client_id)
        if credit is not None:
            self._credit_to_clients[credit].remove(client_id)
            if not self._credit_to_clients[credit]:
                del self._credit_to_clients[credit]
            del self._client_to_credit[client_id]
            return True
        return False

    def lookup(self, client_id):
        credit = self._client_to_credit.get(client_id)
        return -1 if credit is None else credit + self._offset

    def add_all(self, C):
        self._offset += C

    def max(self):
        if not self._credit_to_clients:
            return ''
        clients = self._credit_to_clients.max_item()[1]
        return '' if not clients else next(iter(clients))

test = ClientsCreditInfo()
test.insert('sjc1', 10)
test.insert('sjc2', 20)
test.insert('lax3', 15)
test.insert('jfk20', 40)

print(test.max())
print(test.lookup('lax3'))

test.add_all(10)
test.insert('lax4', 5)
print(test.lookup('sjc1'))
print(test.lookup('lax3'))
print(test.lookup('lax4'))

print(test.remove('jfk20'))