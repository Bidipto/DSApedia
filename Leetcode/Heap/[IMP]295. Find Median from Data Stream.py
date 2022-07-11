#right and left heap combinations 
#where the top of the left heap always gives the ith best location
class MedianFinder:

    def __init__(self):
        self.left = []
        self.L = 0
        self.right = []
        self.R = 0
        
    def addNum(self, num: int) -> None:
        if self.L == self.R:
            heapq.heappush(self.left,-num)
            heapq.heappush(self.right,-heapq.heappop(self.left))
            self.R += 1
        else:
            heapq.heappush(self.right,num)
            heapq.heappush(self.left,-heapq.heappop(self.right))
            self.L += 1  

    def findMedian(self) -> float:
        if self.L == self.R:
            return (float(-self.left[0])+float(self.right[0]))/2
        else:
            return self.right[0]