import requests

class Request:
    def __init__(self,url):
        self._url = url

    def get(self):
        r = requests.get(self._url)
        dictionary_list = r.json()
        return dictionary_list
