from sortedcontainers import SortedList, SortedSet, SortedDict
#first question using this library 
class NumberContainers:

    def __init__(self):
        self.dict = collections.defaultdict(SortedList)
        self.index = {}

    def change(self, index: int, number: int) -> None:
        # print(self.dict,self.index)
        if index in self.index:
            if number != self.index[index]:
                self.dict[self.index[index]].discard(index)
                self.dict[number].add(index)
                self.index[index] = number
                # print(self.dict,self.index)
        else:
            self.dict[number].add(index)
            self.index[index] = number
            # print(self.dict,self.index)
    def find(self, number: int) -> int:
        if self.dict[number]:
            return self.dict[number][0]
        else:
            return -1
        

