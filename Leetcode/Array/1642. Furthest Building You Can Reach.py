# 1642. Furthest Building You Can Reach
def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        #we greedy alot the longest jumps to the ladder using a min heap
        #and then check if until the point brick can help make jumps 
        heap = []
        pre = heights[0]
        for i in range(1,len(heights)):
            curr = heights[i]
            # print(pre,curr,heap,bricks)
            if curr>pre:
                heapq.heappush(heap, curr-pre)
                if len(heap)>ladders:
                    bricks -= heapq.heappop(heap)

                if bricks<0:
                    return i-1
            # print(heap,bricks)
            pre = curr
        return len(heights)-1