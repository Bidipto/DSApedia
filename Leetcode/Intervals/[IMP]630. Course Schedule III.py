# 630. Course Schedule III

def scheduleCourse(self, courses: List[List[int]]) -> int:
        #step one is to sort the cources accoding to their endtime 
        #we will maintain a maxheap with the time required upto and before that element
        #we will also maintain a time to keep track of the the cources that we are takingg
        
        #at any point if we find the start time is more that end time of that ccouse
        #we need to give up on the cource with the longest duration, as it will have
        #the maximum affect on the start time 
        
        heap = []
        start = 0
        for t, end in sorted(courses, key = lambda x: x[1]):
            duration = t
            start += duration
            #negation to covert to max heap 
            heapq.heappush(heap, -duration)
            #when we cont complete a cource we need to give up on cources
            #with the longest duration, and we susbtract it for the start 
            while start>end:
                #adding cause elements are negated while we pushed them 
                start += heapq.heappop(heap)
                
        return len(heap)