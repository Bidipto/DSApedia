# 729. My Calendar I

#we have used binary start on the start arr where the start index of the all events
#are maintained in sorted order 
#we want the pos just to the right of the element smaller the current start 
#and check if it fits right 
class MyCalendar:

    def __init__(self):
        self.list = {}
        self.start = []
        
    def book(self, start: int, end: int) -> bool:
        if not self.list:
            self.list[start] = end
            self.start.append(start)
            return True
        else:
            lo = 0
            hi = len(self.start)
            
            while lo<hi:
                mid = (lo+hi)//2
                if self.start[mid]<start:
                    lo = mid + 1
                else:
                    hi = mid
            # print(self.start,lo,start)
            #when we have to add to end
            if lo == len(self.start):
                if self.list[self.start[lo-1]]<=start:
                    self.start.insert(lo,start)
                    self.list[start] = end 
                    return True
                else:
                    return False
            #when we have to add at the start 
            elif lo == 0:
                if self.start[lo]>=end:
                    self.start.insert(lo,start)
                    self.list[start] = end 
                    return True
                else:
                    return False
            #when we have to add in the middle 
            else:
                if self.list[self.start[lo-1]]<=start and self.start[lo]>=end:
                    self.start.insert(lo,start)
                    self.list[start] = end 
                    return True
                else:
                    return False
            
