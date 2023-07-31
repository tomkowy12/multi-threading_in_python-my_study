import json
import urllib.request
import time
from threading import Thread, Lock

finished_count = 0


def count_letters(url, frequency, mutex):
    global finished_count
    try:
        response = urllib.request.urlopen(url)
    except urllib.error.HTTPError:
        print("Something went wrong with url: {}".format(url))
        finished_count += 1
        return
    txt = str(response.read())
    mutex.acquire()
    for l in txt:
        letter = l.lower()
        if letter in frequency:
            frequency[letter] += 1
    finished_count += 1
    mutex.release()


def main():
    frequency = {}
    mutex = Lock()
    for c in "abcdefghijklmnopqrstuvwxyz":
        frequency[c] = 0
    start = time.time()
    for i in range(34091900, 34091930):  # auch, that hurts, each page separately...
        Thread(target=count_letters, args=(f"https://stackoverflow.com/questions/{i}/", frequency, mutex)).start()
    while True:
        mutex.acquire()
        if finished_count == 20:
            break
        mutex.release()
        time.sleep(0.5)
    end = time.time()
    print(json.dumps(frequency, indent=4))
    print("Done, time taken", end - start)


main()
