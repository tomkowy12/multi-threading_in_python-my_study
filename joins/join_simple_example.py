import time
from threading import Thread


def child():
    print("Child Thread doing work...")
    time.sleep(5)
    print("Child Thread done...")


def parent(case=1):
    t = Thread(target=child, args=([]))
    t.start()
    if case == 1:
        print("Parent Thread is waiting...")
        t.join()
    if case == 2:
        print("Parent Thread is not waiting...")
    print("Parent Thread is unblocked...")


parent()
