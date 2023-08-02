from multiprocessing import Process, Queue
import time

TOTAL_PROCESSES = 12

if __name__ == '__main__':
    queue = Queue(maxsize=1000)
    processes = []
    for i in range(TOTAL_PROCESSES):
        p = Process(target=find_area, args=(queue,))
        processes.append(p)
        p.start()
    f = open("./message_passing/polygons.txt", "r")
    lines = f.read().splitlines()
    start = time.time()
    # queue for sending requests
    for line in lines:
        queue.put(line)
    for _ in range(TOTAL_PROCESSES): queue.put(None)
    for p in processes: p.join()
    # queue for parsing gotten requests
    # data gathering in one DF
    end = time.time()
    print("Time taken", end - start)