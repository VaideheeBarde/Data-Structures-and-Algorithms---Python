#LR and LW are class attributes in the ReaderWriter class
#They serve as read and write locks
#The integer variable read_count in ReaderWriter tracks the number of readers

import threading

class Reader(threading.Thread):

    def run(self):
        while True:
            with ReaderWriter.LR:
                ReaderWriter.read_count += 1

            print(ReaderWriter.data)

            with ReaderWriter.LR:
                ReaderWriter.read_count -= 1
                ReaderWriter.LR.notify()
                
            do_something_else()


class Writer(threading.Thread):
    def run(self):
        while True:
            with ReaderWriter.LW:
                done = False
                while not done:
                    with ReaderWriter.LR:
                        if ReaderWriter.read_count == 0:
                            ReaderWriter.data += 1
                            done = True
                        else:
                            #use wait/notify to avoid busy waiting
                            while ReaderWriter.read_count != 0:
                                ReaderWriter.LR.wait()

            do_something_else()