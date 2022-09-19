import collections
class LruCache:
    def __init__(self, capacity):
        self._isbn_price_table = collections.OrderedDict()
        self._capacity = capacity

    def lookup(self, isbn):
        if isbn not in self._isbn_price_table:
            return -1
        price = self._isbn_price_table.pop(isbn)
        self._isbn_price_table[isbn] = price
        return price

    def insert(self, isbn, price):
        if isbn in self._isbn_price_table:
            price = self._isbn_price_table.pop(isbn)
        elif len(self._isbn_price_table) == self._capacity:
            self._isbn_price_table.popitem()
        self._isbn_price_table[isbn] = price

    def erase(self, isbn):
        return self._isbn_price_table.pop(isbn, None) is not None

lrucache = LruCache(10)
lrucache.insert(7, 12)
print(lrucache._isbn_price_table)
lrucache.insert(6, 51)
lrucache.insert(8, 23)
lrucache.insert(9, 75)
lrucache.insert(13, 51)
print(lrucache._isbn_price_table)
lrucache.insert(15,21)
print(lrucache._isbn_price_table)
lrucache.insert(14,37)
print(lrucache._isbn_price_table)
lrucache.erase(8)
print(lrucache._isbn_price_table)
print(lrucache.lookup(13))
print(lrucache.lookup(1))
lrucache.insert(78, -251)
lrucache.insert(61, 516)
lrucache.insert(62, 531)
lrucache.insert(16, 151)
print(lrucache._isbn_price_table)
lrucache.insert(16, 15)
print(lrucache._isbn_price_table)
lrucache.insert(266666, 1666677751)
print(lrucache._isbn_price_table)
