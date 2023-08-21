class Filter:

    def __init__(self,data):
        self._data = data

    def apply(self,name_chain):
        return self._data.get(name_chain)


