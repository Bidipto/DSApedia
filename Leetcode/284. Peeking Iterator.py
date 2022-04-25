#simplesolution with a buffer read the ps
class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.last = self.iterator.next() if self.iterator.hasNext() else None 
        print(self.last)

    def peek(self):
        return self.last
        

    def next(self):
        res = self.last
        self.last = self.iterator.next() if self.iterator.hasNext() else None 
        return res
    
    def hasNext(self):
        return self.last != None