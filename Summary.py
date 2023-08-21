class Summary:
    
    def __init__(self, data):
        self._data = data
        self._frequencies = {}

    def call(self):
        Summary._build_summary(self)
        return self._frequencies
        
    
    def _process_element(self,dicc):
        
        if self._frequencies.get(dicc['local_nombre']) is None:
            self._frequencies[dicc.get('local_nombre')] = 1

        else:
            self._frequencies[dicc.get('local_nombre')] += 1



    def _build_summary(self):
        
        for local in self._data:
            Summary._process_element(self,local)

