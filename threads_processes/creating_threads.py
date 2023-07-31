import time
from threading import Thread


def do_work(case=2):
    """
    Case 1 is I/O bounded. It will wait 1 sec. while other tasks will start.
    Case 2 is processor bounded. Each process will start, but calculations will
    take some time. There are problems to use all processor power. It is about only 20%,
    and first task will complete when some tasks don't even start. Processor bounded 
    tasks should be handled by processes. 
    """
    print("Starting work")
    if case == 1:
        time.sleep(1)
    elif case == 2:
        i = 0
        for _ in range(20000000):
            i += 1
    print("Finished work")


for _ in range(100):
    # do_work()
    t = Thread(target=do_work, args=())
    t.start()