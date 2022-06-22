# 2054. Two Best Non-Overlapping Events

#uses the opening and closed states
#a little bit unique problem

def maxTwoEvents(self, events: List[List[int]]) -> int:
        arr = []
        for u,v,w in events:
            arr.append((u,w,True))
            arr.append((v+1,w,False))
        arr.sort()
        
        res = 0
        endMax = 0
        
        for start,weight,flag in arr:
            #if the event has stated 
            if flag:
                res = max(res,endMax + weight)
            #if the event has ended
            else:
                endMax = max(endMax, weight)
            
        return res