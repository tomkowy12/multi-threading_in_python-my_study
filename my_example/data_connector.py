import urllib


class DataConnector:
    def __init__(self) -> None:
        pass


    def get_from_url(url: str, filename: str) -> None:
        """
        This method gets file from the URL and saves on disk
        """
        try:
            response = urllib.request.urlopen(url)
        except urllib.error.HTTPError as e:
            print("Something went wrong with url: {}".format(url))
            mutex.acquire()
            should_be_finished -= 1
            mutex.release()
            print(e)
        txt = str(response.read())
        with open(filename, "w") as f:
            f.writelines(txt)