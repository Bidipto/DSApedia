# 2102. Sequentially Ordinal Rank Tracker
# related to the meadian of the data stream 
import heapq
class stringMod():
    def __init__(self, word):
        self.word = word
        
    def __lt__(self, other):
        return self.word>other.word
    
class SORTracker:
    def __init__(self):
        #left is minheap
        self.left = []
        #right is maxheap
        self.right = []
        
    def add(self, name: str, score: int) -> None:
        if not self.left:
            #for first instances before a get is called the left will be empty
            heapq.heappush(self.right, [-score,name])
        elif self.left[0][0]<score or (self.left[0][0] == score and self.left[0][1].word>name):
            #when the current comes before ie higher score or lexiographically smaller name 
            heapq.heappush(self.left, [score,stringMod(name)])
            scoreNew, obj = heapq.heappop(self.left)
            nameNew = obj.word
            heapq.heappush(self.right, [-scoreNew,nameNew])
        else:
            #for lower scores we append to the right
            heapq.heappush(self.right, [-score,name])
            
    def get(self) -> str:
        #we pop the top name from right and append it to left
        score, name = heapq.heappop(self.right)
        heapq.heappush(self.left, [-score,stringMod(name)])
        return name 
        