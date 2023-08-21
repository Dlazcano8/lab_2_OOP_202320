from Request import Request
from Summary import Summary
from Filter import Filter

class Main:

    def __init__(self):
        self._url = 'https://andreshoward.com/pharmacies'

    def main(self,name_chain):

        data = Request(self._url)
    
        s = Summary(data.get())

        f = Filter(s.call())

        print(f.apply(name_chain))

main = Main()

main.main("CRUZ VERDE")

