import threading

class Account:

    _global_id = 0

    def __init__(self, balance):
        self._balance = balance
        self._id = Account._global_id
        Account._global_id += 1
        self._lock = threading.RLock()

    def get_balance(self):
        return self._balance

    @staticmethod
    def transfer(acc_from, acc_to, amount):
        th = threading.Thread(target=acc_from._move, args=(acc_to, amount))
        th.start()

    def _move(self, acc_to, amount):
        lock1 = self._lock if self._id < acc_to._id else acc_to._lock
        lock2 = acc_to._lock if self._id < acc_to._id else self._lock

        #Does not matter if lock1 equals lock2: since recursive_mutex locks
        with lock1, lock2:
            if amount > self._balance:
                return False
            acc_to._balance += amount
            self._balance -= amount
            print('returning True')
            return True

acc1 = Account(100)
acc2 = Account(100)
acc1.transfer(acc1, acc2, 1)
acc3 = Account(100)
acc2.transfer(acc2, acc3, 5)