import multiprocessing

from multiprocessing import Process


def do_work():
    print("Starting work")
    i = 0
    for _ in range(20000000):
        i += 1
    print("Finished work")


if __name__ == '__main__':
    """
    Here we can use all processor power. Memory is not shared. 
    """
    # multiprocessing.set_start_method('spawn')
    multiprocessing.set_start_method('fork')
    for _ in range(100):
        p = Process(target=do_work, args=())
        p.start()
