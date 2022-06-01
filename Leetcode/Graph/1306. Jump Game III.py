# 1306. Jump Game III
# dfs until we reach a zero we have two options at all times 
# go front and go back which acts like two edges
from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start]==0:
            return True
        N = len(arr)
        visited = set([start])
        que = deque([start])
        
        while que:
            node = que.popleft()
            front = node + arr[node]
            back = node - arr[node]
            
            if 0<=front<N and front not in visited:
                if arr[front] == 0:
                    return True
                visited.add(front)
                que.append(front)                
            if 0<=back<N and back not in visited:
                if arr[back] == 0:
                    return True
                visited.add(back)
                que.append(back)
        
        return False