import heapq
from collections import deque
class Solution:
    def racecar(self, target: int) -> int:
        #some greedy modifications 
        
        #we only change direction when the next step will move beyond the target
        #by default we keep moviing in the same direction
        
        #[moves,position,velocity]
        heap = deque([[0,0,1]])
        
        while heap:
            for q in range(len(heap)):
                moves,pos,vel = heap.popleft()
                
                if pos == target:
                    return moves 
                
                heap.append([moves+1,pos+vel,vel*2])
                
                #if we need to move in the negative direction
                if (pos+vel>target and vel>0) or (pos+vel<target and vel<0):
                    heap.append([moves+1,pos,-(vel/abs(vel))])