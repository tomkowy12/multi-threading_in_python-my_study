from multiprocessing import Process, Queue
import time

DATA_URL = "https://media.githubusercontent.com/media/datablist/sample-csv-files/main/files/organizations/organizations-{}.csv"
DATA_NAMES = [100, 1000, 10000, 100000, 500000, 1000000, 2000000]

TOTAL_PROCESSES = 12

if __name__ == '__main__':
    # queue for sending requests
    # what data to acquire?
    # the best are log data! CSVs? TXTs?
    queue = Queue(maxsize=1000)
    processes = []
    for i in range(TOTAL_PROCESSES):
        p = Process(target=send_requests, args=(queue,))
        processes.append(p)
        p.start()
    f = open("./message_passing/polygons.txt", "r")
    lines = f.read().splitlines()
    start = time.time()
    for line in lines:
        queue.put(line)
    for _ in range(TOTAL_PROCESSES): queue.put(None)
    for p in processes: p.join()
    # queue for parsing gotten requests
    # data gathering in one DF
    end = time.time()
    print("Time taken", end - start)