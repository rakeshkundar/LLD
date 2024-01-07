from iterator_interface import Iterator

class BookIterator(Iterator):
    index: int
    data: list()

    def __init__(self, data: list) -> None:
        self.data = data
        self.index = 0

    def has_next(self):
        return self.index < len(self.data)
    
    def next(self):
        if(self.index < len(self.data)):
           value = self.data[self.index]
           self.index += 1
           return value
        
        return None
