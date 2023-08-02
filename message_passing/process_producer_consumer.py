from multiprocessing import Process, Queue

import time


def consumer(q, name):
    while (True):
        txt = q.get()
        print(txt, "in name:", name)
        time.sleep(1)


def producer(q):
    while (True):
        q.put("Hello there")
        print("Message Sent")


if __name__ == '__main__':
    q = Queue(maxsize=10)
    p11 = Process(target=consumer, args=(q,"the first one"))
    p12 = Process(target=consumer, args=(q,"the second one"))
    p2 = Process(target=producer, args=(q,))
    p11.start()
    p12.start()
    p2.start()
