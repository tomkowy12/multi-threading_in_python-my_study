import json
import urllib.request
import time


def count_letters(url, frequency):
    try:
        response = urllib.request.urlopen(url)
    except urllib.error.HTTPError:
        print("Something went wrong with url: {}".format(url))
        return
    txt = str(response.read())
    for l in txt:
        letter = l.lower()
        if letter in frequency:
            frequency[letter] += 1


def main():
    frequency = {}
    for c in "abcdefghijklmnopqrstuvwxyz":
        frequency[c] = 0
    start = time.time()
    for i in range(34091900, 34091930):  # auch, that hurts, each page separately...
        count_letters(f"https://stackoverflow.com/questions/{i}/", frequency)
    end = time.time()
    print(json.dumps(frequency, indent=4))
    print("Done, time taken", end - start)


main()
